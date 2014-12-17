
        # -*- coding: utf-8 -*-
import scrapy

from Informatique.items import harddiskItem

class harddiskSpider(scrapy.Spider):
    name = "harddisks"
    allowed_domains = ["informatique.nl"]
    start_urls = [
    # SATA harddisks
	"http://www.informatique.nl/?m=usl&g=026&view=6&&sort=pop&pl=100",
	# 2.5 inch harddisks
	"http://www.informatique.nl/?m=usl&g=028&view=6&&sort=pop&pl=55",
	# SSD drives
	"http://www.informatique.nl/?m=usl&g=559&view=6&&sort=pop&pl=200",
        ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="content"]/ul/li'):
            item = harddiskItem()
            item['title'] = ''.join(sel.xpath('div[@id="title"]/a/text()').extract())
            item['link'] = ''.join(sel.xpath('div[@id="title"]/a/@href').extract())
            item['price'] = ''.join(sel.xpath('div[@id="price"]/text()').extract())
            item['stock'] = ''.join(sel.xpath('div[@id="stock"]/text()').extract())
            yield item



