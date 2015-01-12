        # -*- coding: utf-8 -*-
import scrapy

from Informatique.items import PowerSupplyItem

class PowersupplySpider(scrapy.Spider):
    name = "powersupply"
    allowed_domains = ["informatique.nl"]
    start_urls = [
        # voedingen
        "http://www.informatique.nl/?m=usl&g=171&view=6&&sort=pop&pl=999",
        ]

    def parse(self, response):
        for sel in response.xpath('//div/div/div[@id="content"]/ul/li'):
            item = PowerSupplyItem()
            item['title'] = ''.join(sel.xpath('div[@id="title"]/a/text()').extract())
            item['image'] = ''.join(sel.xpath('div[@id="image"]/a/img/@src').extract())
            item['link'] = ''.join(sel.xpath('div[@id="title"]/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@id="price"]/text()').extract())
            item['stock'] = ''.join(sel.xpath('div[@id="stock"]/text()').extract())
            yield item



