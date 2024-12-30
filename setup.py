#coding:utf-8

# step1:
#     python setup.py sdist bdist_wheel
#
# step2:
#     C:\Users\admin\AppData\Roaming\Python\Python38\Scripts\twine.exe upload dist/*
# or
#     python -m twine upload dist/*

import os
from setuptools import setup,find_packages,Extension

DIR = os.path.dirname(os.path.abspath(__file__))
# INSTALL_PACKAGES = open(os.path.join(DIR, 'requirements.txt')).read().splitlines()

from lb_toolkits.version import get_versions
__version__ = get_versions()['version']

name = 'lb_toolkits'
description = "lb_toolkits Library for Meteorology and Remote Sensing"
readme = open('README.md', encoding="utf-8").read()
content_type='text/markdown'

setup(
    name = name, # 项目名
    version = __version__, # 如 0.0.1/0.0.1.dev1
    description = description,
    long_description = readme,
    long_description_content_type = content_type,
    # url='', # 如果有github之类的相关链接
    author = 'Nanhu Lab(南湖实验室，聂维)', # 作者
    # author_email='xxx@163.com', # 邮箱
    license = 'MIT',
    platforms = ["windows", 'linux'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/libin033/lb_toolkits',
    keywords=['FengYun', 'Meteorology', 'RemoteSensing',
              'hdf', 'netcdf', 'spider'], # 关键词之间空格相隔一般
    # 需要安装的依赖
    namespace_packages = ['lb_toolkits'],
    install_requires = [
        'numpy >= 1.2.0',
        'tqdm >= 4.0.0',
        'paramiko >= 2.10.0',
        'cdsapi >= 0.5.0',
        'sphinx-rtd-theme >= 1.3',
        'beautifulsoup4>=4.10',
        'geojson>=2.4',
        'geomet>=0.3',
        'html2text>=2',
        'python-dateutil>=2.0',
        'certifi>=2017.4.17',
        'click>=7.1',
    ],
    setup_requires = [

    ],
    packages=find_packages(),
    package_data={
    },
    include_package_data = True, #
    entry_points={ #如果发布的库包括了命令行工具
      },
    package_dir={'lb_toolkits': 'lb_toolkits'},
    python_requires='>=3.7',
)