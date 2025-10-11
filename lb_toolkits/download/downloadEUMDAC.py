# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : downloadEUMDAC.py  
----------------------------------------
@Modify Time : 2025/8/1  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
      
 
'''
import os
import shutil
import sys
import numpy as np
import datetime
import eumdac

URL_LOGIN = r'https://user.eumetsat.int/cas/login'
URL_API_KEY = 'https://api.eumetsat.int/api-key/'


class downloadEUMDAC:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.token = eumdac.AccessToken((self.username, self.password))
        self.datastore = eumdac.DataStore(self.token)

        # self.setCredentials(username, password)

    def setCredentials(self, consumerKey, consumerSecret):
        '''  '''
        print('You can find your ConsumerKey and ConsumerSecret here: https://api.eumetsat.int/api-key/')

        cmd = f'eumdac set-credentials {consumerKey} {consumerSecret}'

        os.system(cmd)

    def searchfile(self, startDate, endDate=None, collection=None,
                   bbox=None, geometry=None, everyday=False,
                   threads=None, options=[]):

        # _query = {
        #     "dtstart": args.dtstart,
        #     "dtend": args.dtend,
        #     "publication": publication,
        #     "bbox": args.bbox,
        #     "geo": args.geo,
        #     "sat": args.sat,
        #     "sort": sort_query,
        #     "cycle": args.cycle,
        #     "orbit": args.orbit,
        #     "relorbit": args.relorbit,
        #     "title": args.filename,
        #     "timeliness": args.timeliness,
        #     "type": args.product_type,
        # }

        selected_collection = self.datastore.get_collection(collection)
        products = selected_collection.search(dtstart=startDate,
                                   dtend=endDate,
                                   bbox=bbox,
                                   geo=geometry)
        for product in products:
            print(product)

        # if endDate is None:
        #     endDate = startDate
        #
        # options.append('-c %s' % collection)
        #
        # if everyday:
        #     options.append('-s %s' %(startDate.strftime('%Y%m%d')))
        #     options.append('-e %s' %(endDate.strftime('%Y%m%d')))
        #
        #     options.append('--daily-window')
        #     options.append(startDate.strftime('%H:%M:%S'))
        #     options.append(endDate.strftime('%H:%M:%S'))
        # else:
        #     options.append('-s %s' %(startDate.strftime('%Y%m%dT%H:%M:%S')))
        #     options.append('-e %s' %(endDate.strftime('%Y%m%dT%H:%M:%S')))
        #
        # if bbox is not None and isinstance(bbox, list):
        #     options.append('--bbox %f %f %f %f ' %(bbox[0], bbox[1], bbox[2], bbox[3]))
        #
        # if geometry is not None:
        #     options.append('--geometry "%s"' %(geometry))
        #
        # if threads is not None:
        #     options.append('--threads %d' %(threads))
        #
        # return ' '.join(options)

    def download(self, outdir, url, progressbar=True):
        # options = ['eumdac download', url]
        # options.append('-o %s' %(outdir))
        # if not progressbar:
        #     options.append('--no-progress-bar')
        #
        # cmd = ' '.join(options)

        for url1 in url:
            with url1.open() as fsrc,\
                    open(fsrc.name, 'wb') as fdst:
                shutil.copyfileobj(fsrc, fdst)
                print('成功下载', url1)


if __name__ == '__main__':
    from lb_toolkits.DataCollections import DataCollections
    startdate = datetime.datetime.strptime('20250731', '%Y%m%d')
    enddate = datetime.datetime.strptime('20250731', '%Y%m%d')

    downloader = downloadEUMDAC(username='ZxijlZP6t_7REMWQyPP6w8hJGAwa',
                                password='aKzno4VAohDyIcoBIprHpOVMPfMa')

    url = downloader.searchfile(startDate=startdate,
                                collection=DataCollections.HIGH_RATE_SEVIRI_LEVEL_15_IMAGE_DATA_MSG_INDIAN_OCEAN_EUMDAC.shortname,
                                )






