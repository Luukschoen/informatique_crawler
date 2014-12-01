        # -*- coding: utf-8 -*-
import scrapy

from project.items import RamddrItem

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
            item['title'] = sel.xpath('div[@id="title"]/a/text()').extract()
            item['link'] = sel.xpath('div[@id="title"]/a/@href').extract()
            item['price'] = sel.xpath('div[@id="price"]/text()').extract()
            item['stock'] = sel.xpath('div[@id="stock"]/text()').extract()
            yield item



