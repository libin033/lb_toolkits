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

    from lb_toolkits.downloadcentre import downloadFY

    mdown = downloadFY(username, password)
    nowdate = datetime.datetime.strptime('20220903 0000', '%Y%m%d %H%M')
    mdown.download_fy_l1(dstpath='./data', starttime=nowdate, geoflag=True)


    mdown = downloadFY(username, password)
    nowdate = datetime.datetime.strptime('20220923 0000', '%Y%m%d %H%M')
    mdown.download_fy_l2(dstpath='./data', satid='FY4B', instid='AGRI', starttime=nowdate, prodid='CTH')


    mdown = downloadFY(username, password)
    nowdate = datetime.datetime.strptime('20220923 0000', '%Y%m%d %H%M')
    mdown.download_fy_l1(dstpath='./data', starttime=nowdate, geoflag=True,
                         satid='FY3D', instid='MERSI', resolution=0.01)

    mdown = downloadFY(username, password)
    nowdate = datetime.datetime.strptime('20220803 0000', '%Y%m%d %H%M')

    # 通过官网下载订单文件下载风云数据
    mdown.download_fy_order('./data', './data/A2022110303128.txt')
    mdown.download_fy_order('./data', orderID='A2022110303128')
    # seachfile('/L2L3')
    #
    # mdown.download_fy_l2(dstpath='./data', starttime=nowdate, prodid='CTH',
    #                      satid='FY3D', instid='MERSI', resolution=0.01)

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

    from lb_toolkits.downloadcentre import downloadH8

    nowdate = datetime.datetime.strptime('20221027', '%Y%m%d')

    down = downh8file(username=FTP_USER, password=FTP_PAWD)
    filelist = down.search_ahi8_l1_netcdf(nowdate)
    down.download('./data', filelist)
    filelist = down.search_ahi8_l1_hsd(nowdate)
    down.download('./data', filelist)

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

    from lb_toolkits.downloadcentre import downloadMODIS
    down = downloadMODIS(username, password)
    nowdate = datetime.datetime.strptime('20180329', '%Y%m%d')
    fils = down.searchfile(nowdate)

    for file in fils :
        print(file)
        down.download(r'./data', file)

downloadTANSAT
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadTANSAT
    down  = downloadTANSAT()
    startdate = datetime.datetime.strptime('20170101', '%Y%m%d')
    enddate = datetime.datetime.strptime('20200601', '%Y%m%d')
    filelist = down.searchfile(startdate, enddate, obstype='ND')
    for item in filelist :
        down.download(r'./data', item)

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
        down.download(r'./data', file)

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

    from lb_toolkits.downloadcentre import downloadSentinel

    down = downloadSentinel(username, password )
    urllist = down.searchfile(starttime=datetime.datetime.utcnow()-datetime.timedelta(days=29),
                    endtime=datetime.datetime.utcnow()-datetime.timedelta(days=28))
    for url in urllist :
        print(url)
        down.download('./data', url)


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
        down.download(r'./data', file)


downloadLandcover
-----------------------------------------

.. code-block:: python

    from lb_toolkits.downloadcentre import downloadLandcover

    down = downloadLandcover()
    fils = down.from_tsinghua(outdir='./data/landcover', minX=100, maxX=110, minY=25, maxY=35)

    urllist = down.from_esri(r'./data/landcover',
                             datetime.datetime.strptime('2021', '%Y'),
                             extent=(70, 20, 120, 55))

