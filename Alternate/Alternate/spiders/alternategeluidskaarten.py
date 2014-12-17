# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import AlternateGeluidskaart

class alternategeluidskaart(scrapy.Spider):
    name = "alternategeluidskaart"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #Geluidskaarten
        "http://www.alternate.nl/html/product/listing.html?navId=17364&navId=17363&navId=17362&tk=7&lk=9517"
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = AlternateGeluidskaart()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            item['link'] = ''.join(sel.xpath('div/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').extract())
            yield item


