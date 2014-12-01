        # -*- coding: utf-8 -*-
import scrapy

from project.items import FanItem

class FanSpider(scrapy.Spider):
    name = "fans"
    allowed_domains = ["informatique.nl"]
    start_urls = [
"http://www.informatique.nl/?m=usl&g=015&view=6&&sort=pop&pl=500",

        ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="content"]/ul/li'):
            item = FanItem()
            item['title'] = sel.xpath('div[@id="title"]/a/text()').extract()
            item['link'] = sel.xpath('div[@id="title"]/a/@href').extract()
            item['price'] = sel.xpath('div[@id="price"]/text()').extract()
            item['stock'] = sel.xpath('div[@id="stock"]/text()').extract()
            yield item



