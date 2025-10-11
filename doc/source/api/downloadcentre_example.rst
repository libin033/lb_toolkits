=================================
downloadcentre调用示例
=================================

downloadCALIPSO
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadCALIPSO

    down = downloadCALIPSO(username, password)
    nowdate = datetime.datetime.strptime('20180329', '%Y%m%d')
    fils = down.searchfile(nowdate)
    for file in fils :
        print(file)
        down.download(r'./data', file)

downloadERA5
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import download_era5_profile, download_era5_surface

    nowdate = datetime.datetime.strptime('20210102', '%Y%m%d')
    # 下载廓线数据
    variable = ['fraction_of_cloud_cover',
                'geopotential',
                'ozone_mass_mixing_ratio',
                'potential_vorticity',
                'relative_humidity',]

    pressure_level = [
        '1', '2', '3',
        '5', '7', '10',
        '20', '30', '50',
        '70', '100', '125',
        '150', '175', '200',]

    download_era5_profile( outname='prof.nc', nowtime=nowdate,
                           variable=variable,
                           pressure=pressure_level)

    # 下载地面数据
    variable = ['2m_dewpoint_temperature',
        '2m_temperature',]

    download_era5_surface(outname='surf.nc', nowtime=nowdate,
                          variable=variable)

downloadFY
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import DownloadCentre
    from lb_toolkits.DataCollections import DataCollections

    downloader = DownloadCentre(DataCollections.FY_Order_NSMC)
    urls = downloader.searchfile(startDate=None,
                                 orderfile=r'A202505230235031087.txt')
    downloader.download(outdir=r'./data', url=urls)

.. code-block:: python

    from lb_toolkits.downloadcentre import DownloadCentre
    from lb_toolkits.DataCollections import DataCollections

    downloader = DownloadCentre(DataCollections.FY_Order_NSMC)
    urls = downloader.searchfile(startDate=None,
                                 orderfile=r'./data/C202505230232030353.txt')

    downloader.download(outdir=r'./data', url=urls)

downloadHY
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadHY

    mdown = downloadHY(username, password)

    startdate = datetime.datetime.strptime('20230209 0000', '%Y%m%d %H%M')
    enddate = datetime.datetime.strptime('20230225 0000', '%Y%m%d %H%M')
    searchfile = mdown.search(starttime=startdate, endtime=enddate, satid='HY2B', instid='SCA', prodid='L2B')

    mdown.download('./data/HY', searchfile)


downloadGFS
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadGFS

    downloadGFS('./data', datetime.datetime.utcnow())

downloadH8
-----------------------------------------

.. code-block:: python

    from lb_toolkits.DataCollections import DataCollections
    from lb_toolkits.downloadcentre import DownloadCentre

    startDate = datetime.datetime.strptime('20250514', '%Y%m%d')
    endDate   = datetime.datetime.strptime('20250516', '%Y%m%d')

    downloader = DownloadCentre(DataCollections.AHI_L1_FLDK_5KM_NC_JMA,
                                username=username_AHI,
                                password=password_AHI)
    urls = downloader.searchfile(startDate = datetime.datetime.strptime('20250514', '%Y%m%d'),
                                 endDate   = datetime.datetime.strptime('20250516', '%Y%m%d'))
    downloader.download(outdir=r'./data/H09', url=urls)

.. code-block:: python

    from lb_toolkits.DataCollections import DataCollections
    from lb_toolkits.downloadcentre import DownloadCentre

    downloader = DownloadCentre(DataCollections.AHI_L1_FLDK_HSD_JMA,
                                username=username_AHI,
                                password=password_AHI)
    urls = downloader.searchfile(startDate=datetime.datetime.strptime('20250524', '%Y%m%d'),
                                 endDate=datetime.datetime.strptime('20250525', '%Y%m%d')-datetime.timedelta(seconds=1),
                                 hoursflag=True)
    downloader.download(outdir=r'./data/H09', url=urls)

.. code-block:: python

    from lb_toolkits.DataCollections import DataCollections
    from lb_toolkits.downloadcentre import DownloadCentre

    downloader = DownloadCentre(DataCollections.AHI_L2_CLP_NC_JMA,
                                username=username_AHI,
                                password=password_AHI)
    urls = downloader.searchfile(startDate=datetime.datetime.strptime('20250524', '%Y%m%d'),
                                 endDate=datetime.datetime.strptime('20250525', '%Y%m%d')-datetime.timedelta(seconds=1),
                                 hoursflag=True)
    downloader.download(outdir=r'./data/H09', url=urls)

downloadLandsat
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadLandsat

    product = 'LANDSAT_8_C1'
    lat = 30.6
    lon = 104.07
    start_date=datetime.datetime.strptime('2020-06-01', '%Y-%m-%d')
    end_date=datetime.datetime.strptime('2022-08-01', '%Y-%m-%d')
    cloud_max = 50
    outdir = './data'

    down = downloadLandsat(username, password)
    Landsat_name = down.searchfile(product, latitude=lat, longitude=lon,
                                   startdate=start_date, enddate=end_date, cloud_cover_max=cloud_max)
    down.download(Landsat_name, outdir)

    # down = downloadLandsat(username_nasa, password_nasa)
    # urllist = down.searchfileByCMR(starttime=start_date, endtime=end_date)
    # for url in urllist :
    #     down.downloadByCMR(outdir, url, skip=True)

downloadMODIS
-----------------------------------------

.. code-block:: python

    from lb_toolkits.DataCollections import DataCollections
    from lb_toolkits.downloadcentre import DownloadCentre

    downer = DownloadCentre(collection=DataCollections.MOD06_L2_V61_LAADS,
                            username=username_nasa,
                            password=password_nasa)
    startdate = datetime.datetime.strptime('20250101', '%Y%m%d')
    enddate = datetime.datetime.strptime('20250102', '%Y%m%d')

    urls = downer.searchfile(startDate=startdate,
                             endDate=enddate,
                             bbox=[102, 28, 106, 32])

    downer.download(outdir=r'./data', url=urls)


downloadEarthdata
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadEarthdata

    down = downloadEarthdata(username=username_nasa, password=password_nasa)

    startdate = datetime.datetime.strptime('20180101', '%Y%m%d')
    enddate = datetime.datetime.strptime('20180103', '%Y%m%d')

    fils = down.searchfile(shortname='MOD35_L2', provider='LAADS',
                           starttime=startdate, endtime=enddate,
                           bounding_box=[100.0, 30.0, 110.0, 50.0])
    for file in fils :
        print(file)
        down.download(outdir=r'./data', url=file)

downloadTANSAT
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadTANSAT
    down  = downloadTANSAT()
    startdate = datetime.datetime.strptime('20170101', '%Y%m%d')
    enddate = datetime.datetime.strptime('20200601', '%Y%m%d')
    filelist = down.searchfile(startdate, enddate, obstype='ND')
    for item in filelist :
        down.download(outdir=r'./data', url=item)

downloadOCO
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadOCO

    down = downloadOCO(username, password)
    nowdate = datetime.datetime.strptime('20210112', '%Y%m%d')
    fils = down.searchfile(nowdate, prodversion='OCO3_L2_Lite_FP')
    # print(fils)
    for file in fils :
        print(file)
        down.download(outdir=r'./data', url=file)

downloadGOSAT
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadGOSAT
    from dateutil.relativedelta import relativedelta
    startdate = datetime.datetime.strptime('20090101', '%Y%m%d')
    enddate = datetime.datetime.strptime('20221101', '%Y%m%d')
    for item in ['CH4', 'CO2'] :
        nowdate = startdate
        while nowdate <= enddate :
            # nowdate = datetime.datetime.strptime('20220101', '%Y%m%d')
            outdir = os.path.join('./data', item)
            downloadGOSAT(outdir=outdir, nowdate=nowdate, prod=item,
                          username=username, password=password)
            nowdate += relativedelta(months=1)

downloadSentinel
-----------------------------------------

.. code-block:: python

    from lb_toolkits.DataCollections import DataCollections
    from lb_toolkits.downloadcentre import DownloadCentre

    down = DownloadCentre(collection=DataCollections.SENTINEL2_S2MSI2A_ESA,
                          username=username_ESA,
                          password=password_ESA)
    starttime=datetime.datetime.strptime('20250511', '%Y%m%d')
    endtime=datetime.datetime.strptime('20250524', '%Y%m%d')

    urls = down.searchfile(startDate=starttime,
                           endDate=endtime,
                           bbox=[110, 25, 111, 26],
                           cloud_cover_max=[0, 30])


    down.download(outdir='./data', url=urls)


downloadDEM
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadDEM

    down = downloadDEM(username=username_nasa, password=password_nasa)

    # 通过CMR查询数据
    fils = down.searchfile( prodversion='ASTGTM_NC')

    # 下载30米DEM数据
    fils = down.searchDEM30M(minX=100, maxX=110, minY=25, maxY=35)

    for file in fils :
        print(file)
        down.download(outdir=r'./data', url=file)


downloadLandcover
-----------------------------------------

.. code-block:: python

    from lb_toolkits.DataCollections import DataCollections
    from lb_toolkits.downloadcentre import DownloadCentre

    startdate = datetime.datetime.strptime('20170101','%Y%m%d')
    enddate   = datetime.datetime.strptime('20230101','%Y%m%d')

    downer = DownloadCentre(DataCollections.LANDCOVER_V003_ESRI)

    urls = downer.searchfile(startDate=startdate, endDate=enddate, bbox=extent=(70, 20, 120, 55))
    downer.download(outdir=r'./data/lc', url=urls)

