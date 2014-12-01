# -*- coding: utf-8 -*-
import scrapy

from project.items import AlternateRam

class alternateram(scrapy.Spider):
    name = "alternateram"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #DDR1
	    "http://www.alternate.nl/html/product/listing.html?navId=11542&tk=7&lk=9335",
        #DDR2
        "http://www.alternate.nl/html/product/listing.html?navId=11554&tk=7&lk=9312",
        #DDR3
        "http://www.alternate.nl/html/product/listing.html?navId=11556&bgid=8296&tk=7&lk=9326",
        #DDR4
        "http://www.alternate.nl/html/product/listing.html?navId=20678&tk=7&lk=13472",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@id="listingResult"]'):
            item = AlternateRam()
            item ['title'] = sel.xpath('div/a/span/span/h2/span/span/text()').extract()
            item ['link'] = sel.xpath('div/a/@href').extract()
            item ['price'] = sel.xpath('div/div/p/span/text()').extract()
            yield item



