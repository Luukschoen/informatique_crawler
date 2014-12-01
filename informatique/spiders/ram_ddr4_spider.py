        # -*- coding: utf-8 -*-
import scrapy

from project.items import RamddrItem

class Ram_ddr4Spider(scrapy.Spider):
    name = "ramddr4"
    allowed_domains = ["informatique.nl"]
    start_urls = [
    # RAM DDR4
	"http://www.informatique.nl/?m=usl&g=725&view=6&&sort=pop&pl=50",

        ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="content"]/ul/li'):
            item = RamddrItem()
            item['title'] = sel.xpath('div[@id="title"]/a/text()').extract()
            item['link'] = sel.xpath('div[@id="title"]/a/@href').extract()
            item['price'] = sel.xpath('div[@id="price"]/text()').extract()
            item['stock'] = sel.xpath('div[@id="stock"]/text()').extract()
            yield item



