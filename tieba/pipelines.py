# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
# from urlparse import urlparse
from os.path import basename,dirname,join
from scrapy.exceptions import DropItem
from scrapy import Request
import json
import codecs


class TiebaPipeline(object):
    def process_item(self, item, spider):
        return item
class MyFilesPipeline(ImagesPipeline):
    # def file_path(self, request, response=None, info=None):
    #     path = urlparse(request.url).path
    #     return join('full', basename(dirname(path)) + ".jpg")
    def get_media_requests(self,item,info): #下载图片
        for image_url in item['image_urls']:
            yield Request(image_url,meta={'item':item,'index':item['image_urls'].index(image_url)})
    def file_path(self,request,response=None,info=None):
        item=request.meta['item'] #通过上面的meta传递过来item
        index=request.meta['index'] #通过上面的index传递过来列表中当前下载图片的下标

        #图片文件名，item['carname'][index]得到汽车名称，request.url.split('/')[-1].split('.')[-1]得到图片后缀jpg,png
        image_guid = item['images_name'][index]+'.'+request.url.split('/')[-1].split('.')[-1]
        #图片下载目录 此处item['country']即需要前面item['country']=''.join()......,否则目录名会变成\u97e9\u56fd\u6c7d\u8f66\u6807\u5fd7\xxx.jpg
        filename = u'full/{0}/{1}'.format(item['author'], image_guid) 
        return filename