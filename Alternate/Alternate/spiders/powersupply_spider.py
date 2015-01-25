# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import PowerSupplyItem

class PowersupplySpider(scrapy.Spider):
    name = "powersupply"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #Voedingen
	    "http://www.alternate.nl/html/product/listing.html?navId=11604&bgid=8215&tk=7&lk=9533",
        ]
        
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = PowerSupplyItem()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            base_url = "http://www.alternate.nl"
            image_url = base_url + sel.xpath('a[@class="productLink"]/span[@class="product"]/span[@class="pic"]/@style').re('\((.*?)\)')[0]
            item['image'] = ''.join(image_url)
            url = base_url + sel.xpath('div/a/@href').extract()[0]
            item['link'] = ''.join(url)
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').re("\\d+"))
            item['product_type'] = ('Voeding')
            item['shop'] = ('Alternate')
            yield item



