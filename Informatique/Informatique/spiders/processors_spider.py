        # -*- coding: utf-8 -*-
import scrapy

from Informatique.items import ProcessorItem

class FanSpider(scrapy.Spider):
    name = "fans"
    allowed_domains = ["informatique.nl"]
    start_urls = [
        "http://www.informatique.nl/?m=usl&g=611&view=6&&sort=pop&pl=80",
        "http://www.informatique.nl/?m=usl&g=218&view=6&&sort=pop&pl=50"

        ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="content"]/ul/li'):
            item = FanItem()
            item['title'] = ''.join(sel.xpath('div[@id="title"]/a/text()').extract())
            item['image'] = ''.join(sel.xpath('div[@id="image"]/a/img/@src').extract())
            item['link'] = ''.join(sel.xpath('div[@id="title"]/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@id="price"]/text()').re("\\d+,\\d+"))
            item['stock'] = ''.join(sel.xpath('div[@id="stock"]/text()').extract())
            yield item



