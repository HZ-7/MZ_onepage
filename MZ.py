# -*- coding: utf-8 -*-
import scrapy

from MZtest.items import MztestItem


class MzSpider(scrapy.Spider):
    name = 'MZ'
    allowed_domains = ['www.meizitu.com']
    start_urls = ['http://www.meizitu.com/a/252.html']
    def parse(self, response):
        title = response.xpath('//*[@id="maincontent"]/div[1]/div[1]/h2/a/text()').extract()[0]
        image_list = response.xpath('//*[@id="maincontent"]/div[2]/p[1]/img')
        for image in image_list:
            image_src = image.css('img::attr(src)').extract()[0]
            item = MztestItem()
            item['image_title'] = title
            item['image_src'] = image_src
            yield item
