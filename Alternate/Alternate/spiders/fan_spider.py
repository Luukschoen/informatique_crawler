# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import FanItem

class FanSpider(scrapy.Spider):
    name = "fans"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #INTEL
	    "http://www.alternate.nl/html/product/listing.html?navId=11626&tk=7&lk=9435",
        #AMD
        "http://www.alternate.nl/html/product/listing.html?navId=11622&tk=7&lk=9419",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = FanItem()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            base_url = "http://www.alternate.nl"
            image_url = base_url + sel.xpath('a[@class="productLink"]/span[@class="product"]/span[@class="pic"]/@style').re('\((.*?)\)')[0]
            item['image'] = ''.join(image_url)
            url = base_url + sel.xpath('div/a/@href').extract()[0]
            item['link'] = ''.join(url)
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').re("\\d+"))
            item['product_type'] = ('Koeling')
            item['shop'] = ('Alternate')
            yield item


