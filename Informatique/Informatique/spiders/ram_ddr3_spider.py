        # -*- coding: utf-8 -*-
import scrapy

from Informatique.items import RamddrItem

class Ram_ddr3Spider(scrapy.Spider):
    name = "ramddr3"
    allowed_domains = ["informatique.nl"]
    start_urls = [
    # RAM DDR3
	"http://www.informatique.nl/?m=usl&g=522&view=6&&sort=pop&pl=407",

        ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="content"]/ul/li'):
            item = RamddrItem()
            item['title'] = ''.join(sel.xpath('div[@id="title"]/a/text()').extract())
            item['image'] = ''.join(sel.xpath('div[@id="image"]/a/img/@src').extract())
            item['link'] = ''.join(sel.xpath('div[@id="title"]/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@id="price"]/text()').re("\\d+,\\d+"))
            item['type'] = ''.join('DDR3')
            item['shop'] = ''.join('Informatique')
            yield item



