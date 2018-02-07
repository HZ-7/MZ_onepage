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
#         获取图片链接
        imgsrc = item['image_src']
#         将链接转交给下载器
        yield scrapy.Request(imgsrc)
        return item
    # def process_item(self, item, spider):
    #     return item

    def item_completed(self, results, item, info):
#         获取图片路径
        image_path = [x['path'] for ok, x in results if ok]
#         分割图片链接，获取图片名称
        image_name = item['image_src'].split('/')[-1]
#         判断文件夹是否存在，存在则存储图片，不存在则创建文件夹
        if not os.path.exists(IMAGES_STORE+item['image_title']):
            os.mkdir(IMAGES_STORE+item['image_title'])
        else:
#         给图片重命名
            os.rename(IMAGES_STORE+image_path[0],IMAGES_STORE+item['image_title']+"/"+image_name)
