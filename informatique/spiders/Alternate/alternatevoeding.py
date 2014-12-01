# -*- coding: utf-8 -*-
import scrapy

from project.items import AlternateVoedingen

class alternatevoedingen(scrapy.Spider):
    name = "alternatevoedingen"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #Voedingen
	    "http://www.alternate.nl/html/product/listing.html?navId=11604&bgid=8215&tk=7&lk=9533",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@id="listingResult"]'):
            item = AlternateVoedingen()
            item ['title'] = sel.xpath('div/a/span/span/h2/span/span/text()').extract()
            item ['link'] = sel.xpath('div/a/@href').extract()
            item ['price'] = sel.xpath('div/div/p/span/text()').extract()
            yield item



