# -*- coding: utf-8 -*-
import scrapy

from project.items import AlternateCases

class alternatecases(scrapy.Spider):
    name = "alternatecases"
    allowed_domains = ["alternate.nl"]
    start_urls = [
    	# behuizingen
        "http://www.alternate.nl/html/product/listing.html?navId=2436&bgid=8148&tk=7&lk=9309",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@id="listingResult"]'):
            item = AlternateCases()
            item['title'] = sel.xpath('div/a/span/span/h2/span/span/text()').extract()
            item['link'] = sel.xpath('div/a/@href').extract()
            item['price'] = sel.xpath('div/div/p/span/text()').extract()
            yield item


