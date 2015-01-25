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
            base_url = "http://www.alternate.nl"
            image_url = base_url + sel.xpath('a[@class="productLink"]/span[@class="product"]/span[@class="pic"]/@style').re('\((.*?)\)')[0]
            item['image'] = ''.join(image_url)
            url = base_url + sel.xpath('div/a/@href').extract()[0]
            item['link'] = ''.join(url)
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').re("\\d+"))
            item['product_type'] = ('Schijf')
            item['shop'] = ('Alternate')
            yield item



