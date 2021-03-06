        # -*- coding: utf-8 -*-
import scrapy

from Informatique.items import RamddrItem

class Ram_ddr2Spider(scrapy.Spider):
    name = "ramddr2"
    allowed_domains = ["informatique.nl"]
    start_urls = [
    # RAM DDR2
	"http://www.informatique.nl/?M=USL&G=194",
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="content"]/ul/li'):
            item = RamddrItem()
            item['title'] = ''.join(sel.xpath('div[@id="title"]/a/text()').extract())
            item['image'] = ''.join(sel.xpath('div[@id="image"]/a/img/@src').extract())
            item['link'] = ''.join(sel.xpath('div[@id="title"]/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@id="price"]/text()').re("\\d+,\\d+"))
            item['type'] = ''.join('DDR2')
            item['shop'] = ''.join('Informatique')
            yield item



