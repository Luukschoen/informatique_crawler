        # -*- coding: utf-8 -*-
import scrapy

from Informatique.items import RamddrItem

class Ram_ddr1Spider(scrapy.Spider):
    name = "ramddr1"
    allowed_domains = ["informatique.nl"]
    start_urls = [
    # RAM DDR1
	"http://www.informatique.nl/?M=ART&G=077",
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="content"]/ul/li'):
            item = RamddrItem()
            item['title'] = ''.join(sel.xpath('div[@id="title"]/a/text()').extract())
            item['link'] = ''.join(sel.xpath('div[@id="title"]/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@id="price"]/text()').extract())
            item['stock'] = ''.join(sel.xpath('div[@id="stock"]/text()').extract())
            yield item



