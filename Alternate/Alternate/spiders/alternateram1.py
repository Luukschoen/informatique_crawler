# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import AlternateRam1

class alternateram1(scrapy.Spider):
    name = "alternateram1"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #DDR1
	    "http://www.alternate.nl/html/product/listing.html?navId=11542&tk=7&lk=9335",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = AlternateRam1()
            item['title'] = sel.xpath('a/span/span/h2/span/span/text()').extract()
            item['link'] = sel.xpath('div/a/@href').extract()
            item['price'] = sel.xpath('div[@class="waresSum"]/p/span/text()').extract()
            yield item



