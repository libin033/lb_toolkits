=================================
tools调用示例
=================================

spider
-----------------------------------------

.. code-block:: python

    from lb_toolkits.tools import spidertable

    url = 'http://fy4.nsmc.org.cn/data/en/data/realtime.html'
    spidertable(url, './data/FY4A.xls')

nc2tif
-----------------------------------------

.. code-block:: python

        from lb_toolkits.tools import nc2tif

        filename = r'./L3m_20210607__171505720_4_AV-OLB_ZSD_DAY_00.nc'
        nc2tif('./data/test.tif', filename, 'ZSD_mean')

gifpro
-----------------------------------------

.. code-block:: python


        from lb_toolkits.tools import creategif1, splitgif

        pathin = r'./images'

        fils = glob.glob(os.path.join(pathin, '*.PNG'))
        fils.sort()
        creategif1('./data/test.gif', filelist=fils, duration=1 / 2.0)

        splitgif('./data/', './data/test.gif')

wget
-----------------------------------------

.. code-block:: python

    wget(outdir, url, username=None, password=None, token=None,
         tries=3, skip=False, cover=False, options=None)

