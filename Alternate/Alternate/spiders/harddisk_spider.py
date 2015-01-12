# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import harddiskItem

class harddiskSpider(scrapy.Spider):
    name = "harddisks"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        # SATA harddisks
	    "http://www.alternate.nl/html/product/listing.html?navId=11584&bgid=8459&tk=7&lk=9563",
        # SSD drives
        "http://www.alternate.nl/html/highlights/page.html?hgid=217&tgid=967&tk=7&lk=9581"
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = harddiskItem()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            #only do this one if it's available
            item['link'] = ''.join(sel.xpath('div/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').extract())
            yield item



