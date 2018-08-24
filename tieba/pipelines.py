# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from urlparse import urlparse
from os.path import basename,dirname,join


class TiebaPipeline(object):
    def process_item(self, item, spider):
        return item
class MyFilesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        return join('full', basename(dirname(path)) + ".jpg")