# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import AlternateMoederbord

class alternatemoederbord(scrapy.Spider):
    name = "alternatemoederbord"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #INTEL
	    "http://www.alternate.nl/html/product/listing.html?navId=11626&tk=7&lk=9435",
        #AMD
        "http://www.alternate.nl/html/product/listing.html?navId=11622&tk=7&lk=9419",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = AlternateMoederbord()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            item['link'] = ''.join(sel.xpath('div/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').extract())
            yield item


