# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : ftppro.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :
通过ftplib进行ftp文件上传和下载
'''
import errno
import ftplib
import os
import datetime
import re
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class ftppro():

    def __init__(self, ip, user=None, password=None, TLSFlag=False):
        logger.info('正在连接【%s】' %(ip))
        self.host = ip
        self.user = user
        self.pwd = str(password)
        self.ftp = None
        self.TLSFlag = TLSFlag

        self.connect()

    def connect(self, timeout=5*60):

        connflag = False
        try:
            self.ftp.voidcmd("NOOP")
            connflag = True
        except BaseException as e:
            connflag = False

        try:
            if connflag :
                return self.ftp
            else:
                if self.TLSFlag :
                    ftp = ftplib.FTP_TLS(self.host, timeout=timeout)
                else:
                    ftp = ftplib.FTP(self.host, timeout=timeout)
                ftp.encoding = 'utf'

                if self.user is None or self.pwd is None :
                    ftp.login('anonymous', '')
                else:
                    ftp.login(self.user, self.pwd)

                if self.TLSFlag :
                    ftp.prot_p()  # 启用数据通道加密

                self.ftp = ftp

                return ftp
        except BaseException as e:
            logger.error('连接失败【%s】' % self.host)
            # ftp.quit()
            return None

    def downloadFile(self, remoteFile, localPath, blocksize=1*1024, skip_download=False, cover=False):
        '''
        通过ftp下载文件

        Parameters
        ----------
        remoteFile: str
        localPath : str
        blocksize
        skip_download : bool
            是否跳过下载文件，TRUE则不下载文件，直接返回文件名，否则，下载该文件

        cover : bool
            文件存在，
            如果cover为TRUE，则删除原文件后重新下载,
            如果cover为FALSE，就跳过该文件下载

        Returns
        -------

        '''

        localFile = os.path.join(localPath, os.path.basename(remoteFile))
        # 文件存在，如果skip为TRUE，就跳过该文件下载，
        # 如果skip为FALSE，则删除原文件后重新下载
        if skip_download :
            return localFile

        # 文件存在，是否需要覆盖下载
        if os.path.isfile(localFile):
            if cover :
                os.remove(localFile)
                logger.warning('文件已存在，删除该文件后重新下载【%s】' %(localFile))
            else:
                logger.info('文件已存在，跳过下载该文件【%s】' %(localFile))
                return localFile


        tempfile = localFile + '.download'

        self.__makedir(localPath)

        try:
            ftp = self.connect()
            if ftp is None :
                return None
            self._download(ftp, tempfile, remoteFile, blocksize=blocksize)

            # 把之前下载的文件删除后进行重命名
            if os.path.isfile(localFile):
                os.remove(localFile)

            if os.path.isfile(tempfile) :
                os.rename(tempfile, localFile)
            return localFile
        except BaseException as e:
            logger.warning(e)
            logger.warning('下载文件失败,再尝试下载【%s】' %(localFile))

            try:
                ftp = self.connect()
                if ftp is None :
                    return None
                self._download(ftp, tempfile, remoteFile, blocksize=blocksize)
                if os.path.isfile(tempfile) :
                    os.rename(tempfile, localFile)
                return localFile
            except BaseException as e:
                logger.error(e)
                logger.warning('再次下载文件失败【%s】' %(localFile))
                if os.path.isfile(tempfile) :
                    os.remove(tempfile)
            return None

    def uploadFile(self, localfile, remotePath, cover=True, blocksize = 1 * 1024):
        '''
        上传文件
        【注意】：本功能未经过测试验证可行性

        Parameters
        ----------
        localfile: str
            本地存储路径
        remotePath: str
            远程上传路径
        remoteFile: str
            远程文件
        block_size: int
            上传块大小，单位：byte

        Returns
        -------

        '''

        ftp = self.connect()
        if ftp is None :
            return False

        ftp.voidcmd('TYPE I')
        basename = os.path.basename(localfile)
        remoteFile = os.path.join(remotePath, basename)
        remoteFile = remoteFile.replace('\\','/')

        remotePath = remotePath.replace('\\','/')
        self.__makeRemoteDir(remotePath)

        self._upload(ftp, localfile, remoteFile, cover=cover, blocksize=blocksize)


    def _upload(self, ftp, localfile, remotefile, cover=True, blocksize=1024):

        basename = os.path.basename(localfile)

        localsize = os.path.getsize(localfile)
        if self._judge_remotefile_exist(ftp, remotefile):
            ftp.voidcmd('TYPE I')
            remotesize = ftp.size(remotefile)
        else:
            remotesize = 0

        if localsize == remotesize :
            if cover :
                remotesize = 0
            else:
                logger.info('远程文件已存在，跳过上传【%s】' %(remotefile))
                return remotefile

        try:
            with open(localfile, 'rb') as fp:
                from tqdm import tqdm
                with tqdm(
                        total=localsize, unit="B", unit_scale=True, desc=f"正在上传【{basename}】",
                        unit_divisor=blocksize, initial=remotesize
                ) as pbar:
                    ftp.voidcmd('TYPE I')
                    datasock, esize = ftp.ntransfercmd("STOR %s" % remotefile, remotesize)
                    fp.seek(remotesize)

                    def callback(block):
                        datasock.sendall(block)
                        pbar.update(len(block))

                    while True:
                        data = fp.read(blocksize)
                        if not data:
                            break

                        callback(data)
                        remotesize += len(data)

                    if remotesize != localsize :
                        logger.error('上传文件失败【%s】' %(remotefile))
                try:
                    import ssl
                except ImportError:
                    _SSLSocket = None
                else:
                    _SSLSocket = ssl.SSLSocket

                datasock.close()
                # shutdown ssl layer
                # if _SSLSocket is not None and isinstance(conn, _SSLSocket):
                #     conn.unwrap()

            # with open(localfile, "rb") as fp:
            #     fp.seek(remotesize)
            #     ftp.storbinary("STOR %s" % remotePath, fp, block_size)
        except BaseException as e:
            logger.error(e)
            error_code = str(e).split()[0]
            if error_code == '451':
                logger.warning('重新上传文件【%s】' %(localfile))
                ftp.voidcmd('TYPE I')
                with open(localfile, "rb") as fp:
                    ftp.storbinary(f"STOR {remotefile}", fp)
            elif error_code == '550':
                logger.error(f"错误 ({error_code}): 操作不允许 - {str(e)}")

                # 检查是否有读取权限
                if self.check_read_permission(ftp, remotefile):
                    logger.warning("有读取权限，尝试删除并重新上传...")
                    try:
                        ftp.delete(remotefile)
                        logger.info(f"已删除现有文件: {remotefile}")
                    except ftplib.error_perm:
                        logger.warning("无法删除文件，可能没有权限")
                else:
                    logger.warning("没有读取权限，请检查用户权限")
                    return None
            else:
                logger.error(f"其他FTP权限错误 ({error_code}): {str(e)}")
                return None

        ftp.voidresp()
        return remotefile

    def __makedir(self,dirname):
        if not os.path.isdir(dirname):
            os.makedirs(dirname)

    def check_read_permission(self, ftp, dir_path):
        """检查是否有读取目录的权限"""
        try:
            ftp.cwd(dir_path)
            ftp.retrlines('LIST')
            return True
        except ftplib.error_perm:
            return False


    def list_dir_regex(self, remotePath, regexStr):
        ftp = self.connect()
        try:
            ftp.cwd(remotePath)
            fileList = ftp.nlst()

            p = re.compile(regexStr)
            matchedFiles = []
            for file in fileList:
                match = p.search(file)
                if match:
                    matchedFiles.append(match.string)

            return matchedFiles
        except BaseException as e:
            logger.warning(e)


    def listdir(self, dirname, pattern=None):
        ftp = self.connect()
        try:
            ftp.cwd(dirname)
            if pattern is None :
                fileList = ftp.nlst()
            else:
                fileList = ftp.nlst(pattern)
            return fileList

        except BaseException as e:
            return []

    def __makeRemoteDir(self, dirPath):
        ftp = self.connect()
        current_dir = ftp.pwd()

        dirs = dirPath.split('/')

        for dirName in dirs:
            if dirName:
                try:
                    if dirName == 'home':
                        ftp.cwd( '/' + dirName)
                    else:
                        ftp.cwd(dirName)
                except Exception as e:
                    try:
                        ftp.mkd(dirName)
                        ftp.cwd(dirName)
                    except ftplib.error_perm:
                        raise PermissionError(f"无法创建目录: {dirName}")
        # 切换至根目录
        ftp.cwd(current_dir)


    def _download(self, ftp, tempfile, remoteFile, blocksize=1024, continuing=False):
        ''' 下载文件 '''
        ftp.voidcmd('TYPE I')
        basename = os.path.basename(remoteFile)
        def callback(block):
            fp.write(block)
            pbar.update(len(block))


        if continuing and os.path.isfile(tempfile):
            already_downloaded_bytes = os.path.getsize(tempfile)
            continuing = True
        else:
            continuing = False
            already_downloaded_bytes = 0

        remotesize = ftp.size(remoteFile)

        mode = "ab" if continuing else "wb"

        with open(tempfile, mode) as fp:
            from tqdm import tqdm
            with tqdm(
                    total=remotesize, unit="B", unit_scale=True, desc=f"正在下载【{basename}】",
                    unit_divisor=blocksize, initial=already_downloaded_bytes
            ) as pbar:

                with ftp.transfercmd('RETR %s' % (remoteFile), already_downloaded_bytes) as conn:
                    while 1:
                        data = conn.recv(blocksize)
                        if not data:
                            break
                        callback(data)

            try:
                import ssl
            except ImportError:
                _SSLSocket = None
            else:
                _SSLSocket = ssl.SSLSocket
            # shutdown ssl layer
            if _SSLSocket is not None and isinstance(conn, _SSLSocket):
                conn.unwrap()

        return ftp.voidresp()


    def _judge_remotefile_exist(self, ftp, remotefile):

        try:
            if remotefile in ftp.nlst(os.path.dirname(remotefile)):
                return True
            else:
                return False
        except BaseException as e:
            return False


    def close(self, ftp):
        if ftp is not None:
            ftp.quit()
            ftp = None

    def __del__(self):
        if self.ftp is not None:
            self.ftp.quit()
            self.ftp = None
