# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import VideocardItem

class VideocardSpider(scrapy.Spider):
    name = "videocards"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #Geluidskaarten
        "http://www.alternate.nl/html/product/listing.html?navId=11606&bgid=11369&tk=7&lk=9374",
        "http://www.alternate.nl/html/product/listing.html?filter_5=&filter_4=&filter_3=&filter_2=&filter_1=&size=500&bgid=10846&lk=9365&tk=7&navId=11608#listingResult"
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listRow"]'):
            item = VideocardItem()
            item['title'] = ''.join(sel.xpath('a/span/span/h2/span/span/text()').extract())
            base_url = "http://www.alternate.nl"
            image_url = base_url + sel.xpath('a[@class="productLink"]/span[@class="product"]/span[@class="pic"]/@style').re('\((.*?)\)')[0]
            item['image'] = ''.join(image_url)
            url = base_url + sel.xpath('div/a/@href').extract()[0]
            item['link'] = ''.join(url)
            item['price'] = ''.join(sel.xpath('div[@class="waresSum"]/p/span/text()').re("\\d+"))
            item['product_type'] = ('Videokaart')
            item['shop'] = ('Alternate')
            yield item


