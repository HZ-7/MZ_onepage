# -*- coding: utf-8 -*-
import scrapy

from MZtest.items import MztestItem


class MzSpider(scrapy.Spider):
    name = 'MZ'
    allowed_domains = ['www.meizitu.com']
    start_urls = ['http://www.meizitu.com/a/252.html']
    def parse(self, response):
#       获取图片标题，此标题也将用来命名图片保存的文件夹
        title = response.xpath('//*[@id="maincontent"]/div[1]/div[1]/h2/a/text()').extract()[0]
#       获取图片链接<selector>
        image_list = response.xpath('//*[@id="maincontent"]/div[2]/p[1]/img')
#       循环遍历选择器，将存储信息放入item
        for image in image_list:
            image_src = image.css('img::attr(src)').extract()[0]
            item = MztestItem()
            item['image_title'] = title
            item['image_src'] = image_src
            yield item

            
#     yied item将item提交给管道，管道利用item获取图片链接，将链接提交给下载器，下载器将图片保存在setting文件中设置的位置中，并创建一个full子文件夹
