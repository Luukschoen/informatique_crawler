# -*- coding: utf-8 -*-
import scrapy

from project.items import CasesItem

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
            item['title'] = sel.xpath('div[@id="title"]/a/text()').extract()
            item['link'] = sel.xpath('div[@id="title"]/a/@href').extract()
            item['price'] = sel.xpath('div[@id="price"]/text()').extract()
            item['stock'] = sel.xpath('div[@id="stock"]/text()').extract()
            yield item


