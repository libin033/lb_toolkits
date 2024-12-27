=================================
utils调用示例
=================================

spider
-----------------------------------------

.. code-block:: python

    from lb_toolkits.utils import spidertable

    url = 'http://fy4.nsmc.org.cn/data/en/data/realtime.html'
    spidertable(url, './data/FY4A.xls')


wget
-----------------------------------------

.. code-block:: python

    wget(outdir, url, username=None, password=None, token=None,
         tries=3, skip=False, cover=False, options=None)

