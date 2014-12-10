# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import AlternateRam4

class alternateram4(scrapy.Spider):
    name = "alternateram4"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #DDR4
        "http://www.alternate.nl/html/product/listing.html?navId=20678&tk=7&lk=13472",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = AlternateRam4()
            item['title'] = sel.xpath('a/span/span/h2/span/span/text()').extract()
            item['link'] = sel.xpath('div/a/@href').extract()
            item['price'] = sel.xpath('div[@class="waresSum"]/p/span/text()').extract()
            yield item


