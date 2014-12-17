# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import AlternateVoedingen

class alternatevoedingen(scrapy.Spider):
    name = "alternatevoedingen"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #Voedingen
	    "http://www.alternate.nl/html/product/listing.html?navId=11604&bgid=8215&tk=7&lk=9533",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = AlternateVoedingen()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            item['link'] = ''.join(sel.xpath('div/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').extract())
            yield item



