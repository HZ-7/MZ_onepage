# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy,os
from MZtest.settings import IMAGES_STORE
class MztestPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        imgsrc = item['image_src']
        yield scrapy.Request(imgsrc)
        return item
    # def process_item(self, item, spider):
    #     return item

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        image_name = item['image_src'].split('/')[-1]
        if not os.path.exists(IMAGES_STORE+item['image_title']):
            os.mkdir(IMAGES_STORE+item['image_title'])
        else:
            os.rename(IMAGES_STORE+image_path[0],IMAGES_STORE+item['image_title']+"/"+image_name)