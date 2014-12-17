# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import AlternateRam2

class alternateram2(scrapy.Spider):
    name = "alternateram2"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #DDR2
        "http://www.alternate.nl/html/product/listing.html?navId=11554&tk=7&lk=9312",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = AlternateRam2()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            item['link'] = ''.join(sel.xpath('div/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').extract())
            yield item



