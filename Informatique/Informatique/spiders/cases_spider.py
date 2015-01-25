# -*- coding: utf-8 -*-
import scrapy
import uuid

from Informatique.items import CasesItem

class CasesSpider(scrapy.Spider):
    name = "cases"
    allowed_domains = ["informatique.nl"]
    start_urls = [
    	# behuizingen
        "http://www.informatique.nl/?m=usl&g=004&view=6&&sort=pop&pl=999",
        ]
    def parse(self, response):
        for sel in response.xpath('//div/div/div[@id="content"]/ul/li'):
            item = CasesItem()
            item['title'] = ''.join(sel.xpath('div[@id="title"]/a/text()').extract())
            item['image'] = ''.join(sel.xpath('div[@id="image"]/a/img/@src').extract())
            item['link'] = ''.join(sel.xpath('div[@id="title"]/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@id="price"]/text()').re("\\d+,\\d+"))
            item['stock'] = ''.join(sel.xpath('div[@id="stock"]/text()').extract())
            item['product_type'] = ('Behuizingen')
            item['shop'] = ('Informatique')
            yield item


