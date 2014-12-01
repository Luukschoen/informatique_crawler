# -*- coding: utf-8 -*-
import scrapy

from project.items import AlternateMoederbord

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
        for sel in response.xpath('//div[@id="listingResult"]'):
            item = AlternateMoederbord()
            item ['title'] = sel.xpath('div/a/span/span/h2/span/span/text()').extract()
            item ['link'] = sel.xpath('div/a/@href').extract()
            item ['price'] = sel.xpath('div/div/p/span/text()').extract()
            yield item



