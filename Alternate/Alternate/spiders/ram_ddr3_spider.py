# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import RamddrItem

class Ram_ddr3Spider(scrapy.Spider):
    name = "ramddr3"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #DDR3
        "http://www.alternate.nl/html/product/listing.html?navId=11556&bgid=8296&tk=7&lk=9326",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = RamddrItem()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            item['capacity'] = ''.join(sel.xpath('a/span[2]/text()').extract())
            base_url = "http://www.alternate.nl"
            image_url = base_url + sel.xpath('a[@class="productLink"]/span[@class="product"]/span[@class="pic"]/@style').re('\((.*?)\)')[0]
            item['image'] = ''.join(image_url)
            url = base_url + sel.xpath('div/a/@href').extract()[0]
            item['link'] = ''.join(url)
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').re("\\d+"))
            item['type'] = ''.join('DDR3')
            item['product_type'] = ('RAM')
            item['shop'] = ('Alternate')
            yield item




