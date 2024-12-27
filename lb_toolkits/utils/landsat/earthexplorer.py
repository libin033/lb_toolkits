"""Handle login and downloading from the EarthExplorer portal."""

import os
import re
import shutil
import requests
from tqdm import tqdm

from lb_toolkits.utils.landsat import API
from lb_toolkits.utils.landsat import EarthExplorerError
from lb_toolkits.utils.landsat import guess_dataset, is_display_id


EE_URL = "https://earthexplorer.usgs.gov/"
EE_LOGIN_URL = "https://ers.cr.usgs.gov/login/"
EE_LOGOUT_URL = "https://earthexplorer.usgs.gov/logout"
EE_DOWNLOAD_URL = (
    "https://earthexplorer.usgs.gov/download/{data_product_id}/{entity_id}/EE/"
)

# IDs of GeoTIFF data product for each dataset
DATA_PRODUCTS = {
    # Level 1 datasets
    "landsat_tm_c2_l1": ["5e81f14f92acf9ef", "5e83d0a0f94d7d8d", "63231219fdd8c4e5"],
    "landsat_etm_c2_l1":[ "5e83d0d0d2aaa488", "5e83d0d08fec8a66"],
    "landsat_ot_c2_l1": ["5e81f14ff4f9941c", "5e81f14f92acf9ef"],
    # Level 2 datasets
    "landsat_tm_c2_l2": ["5e83d11933473426", "5e83d11933473426", "632312ba6c0988ef"],
    "landsat_etm_c2_l2": ["5e83d12aada2e3c5", "5e83d12aed0efa58", "632311068b0935a8"],
    "landsat_ot_c2_l2": ["5e83d14f30ea90a9", "5e83d14fec7cae84", "632210d4770592cf"]
}

def _get_token(body):
    """Get `csrf_token`."""
    csrf = re.findall(r'name="csrf" value="(.+?)"', body)[0]
    
    if not csrf:
        raise EarthExplorerError("EE: login failed (csrf token not found).")

    return csrf

class EarthExplorer(object):
    """Access Earth Explorer portal."""

    def __init__(self, username, password):
        """Access Earth Explorer portal."""
        self.session = requests.Session()
        self.login(username, password)
        self.api = API(username, password)

    def logged_in(self):
        """Check if the log-in has been successfull based on session cookies."""
        eros_sso = self.session.cookies.get("EROS_SSO_production_secure")
        return bool(eros_sso)

    def login(self, username, password):
        """Login to Earth Explorer."""
        rsp = self.session.get(EE_LOGIN_URL)
        csrf = _get_token(rsp.text)
        payload = {
            "username": username,
            "password": password,
            "csrf": csrf,
        }
        rsp = self.session.post(EE_LOGIN_URL, data=payload, allow_redirects=True)

        if not self.logged_in():
            raise EarthExplorerError("EE: login failed.")

    def logout(self):
        """Log out from Earth Explorer."""
        self.session.get(EE_LOGOUT_URL)
    
    def _download(
        self, url, outdir, timeout, chunk_size=1024, skip_download=False, cover=False
    ):
        """Download remote file given its URL."""
        # Check availability of the requested product
        # EarthExplorer should respond with JSON
        with self.session.get(
            url, allow_redirects=False, stream=True, timeout=timeout
        ) as r:
            r.raise_for_status()
            error_msg = r.json().get("errorMessage")
            if error_msg:
                raise EarthExplorerError(error_msg)
            download_url = r.json().get("url")

        try:
            local_filename, filesize = self._get_fileinfo(
                download_url, timeout=timeout, output_dir=outdir
            )

            if skip_download:
                return local_filename

            if os.path.isfile(local_filename) :
                print('文件已存在，跳过下载【%s】' %(local_filename))
                return local_filename

            basename = os.path.basename(local_filename)
            tempfile = os.path.join(outdir, basename + '.download')

            headers = {}
            file_mode = "wb"
            downloaded_bytes = 0
            file_exists = os.path.exists(tempfile)

            if file_exists and not cover:
                downloaded_bytes = os.path.getsize(tempfile)
                headers = {"Range": f"bytes={downloaded_bytes}-"}
                file_mode = "ab"
            if file_exists and downloaded_bytes == filesize:
                # assert file is already complete
                shutil.move(tempfile, local_filename)
                return local_filename


            with self.session.get(
                download_url,
                stream=True,
                allow_redirects=True,
                headers=headers,
                timeout=timeout,
            ) as r:
                with tqdm(
                    total=filesize,
                    unit_scale=True,
                    unit="B",
                    desc=f"正在下载【{basename}】",
                    unit_divisor=1024,
                    initial=downloaded_bytes
                ) as pbar:
                    with open(tempfile, file_mode) as f:
                        for chunk in r.iter_content(chunk_size=chunk_size):
                            if chunk:
                                f.write(chunk)
                                pbar.update(chunk_size)

            shutil.move(tempfile, local_filename)
            return local_filename

        except requests.exceptions.Timeout:
            raise EarthExplorerError(
                "连接超时【{}秒】".format(timeout)
            )

    def _get_fileinfo(self, download_url, timeout, output_dir):
        """Get file name and size given its URL."""
        try:
            with self.session.get(
                download_url, stream=True, allow_redirects=True, timeout=timeout
            ) as r:
                file_size = int(r.headers.get("Content-Length"))
                local_filename = r.headers["Content-Disposition"].split("=")[-1]
                local_filename = local_filename.replace('"', "")
                local_filename = os.path.join(output_dir, local_filename)
        except requests.exceptions.Timeout:
            raise EarthExplorerError(
                "Connection timeout after {} seconds.".format(timeout)
            )
        return local_filename, file_size

    def download(
        self,
        identifier,
        outdir,
        dataset=None,
        timeout=300,
        skip_download=False,
        cover=False,
    ):
        """Download a Landsat scene.

        Parameters
        ----------
        identifier : str
            Scene Entity ID or Display ID.
        outdir : str
            Output directory. Automatically created if it does not exist.
        dataset : str, optional
            Dataset name. If not provided, automatically guessed from scene id.
        timeout : int, optional
            Connection timeout in seconds.
        skip_download : bool, optional
            Skip download, only returns the remote filename.

        Returns
        -------
        filename : str
            Path to downloaded file.
        """
        os.makedirs(outdir, exist_ok=True)
        if not dataset:
            dataset = guess_dataset(identifier)
        if is_display_id(identifier):
            entity_id = self.api.get_entity_id(identifier, dataset)
        else:
            entity_id = identifier
        # Cycle through the available dataset ids until one works
        dataset_id_list = DATA_PRODUCTS[dataset]
        id_num = len(dataset_id_list)
        for id_count, dataset_id in enumerate(dataset_id_list):
            try:
                url = EE_DOWNLOAD_URL.format(
                    data_product_id=dataset_id, entity_id=entity_id
                )
                filename = self._download(
                    url, outdir, timeout=timeout, skip_download=skip_download, cover=cover
                )
            except EarthExplorerError:
                if id_count+1 < id_num:
                    # print('Download failed with dataset id {:d} of {:d}. Re-trying with the next one.'.format(id_count+1, id_num))
                    pass
                else:
                    # print('None of the archived ids succeeded! Update necessary!')
                    # raise EarthExplorerError()
                    return None
        return filename
