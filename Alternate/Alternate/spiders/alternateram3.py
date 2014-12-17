# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import AlternateRam3

class alternateram3(scrapy.Spider):
    name = "alternateram3"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #DDR3
        "http://www.alternate.nl/html/product/listing.html?navId=11556&bgid=8296&tk=7&lk=9326",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = AlternateRam3()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            item['link'] = ''.join(sel.xpath('div/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').extract())
            yield item




