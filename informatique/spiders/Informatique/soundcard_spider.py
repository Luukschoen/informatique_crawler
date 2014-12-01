# -*- coding: utf-8 -*-
import scrapy

from project.items import SoundcardItem

class MotherboardSpider(scrapy.Spider):
    name = "soundcards"
    allowed_domains = ["informatique.nl"]
    start_urls = [
	"http://www.informatique.nl/?m=art&g=023&view=6&&sort=pop&pl=50",

        ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="content"]/ul/li'):
            item = SoundcardItem()
            item['title'] = sel.xpath('div[@id="title"]/a/text()').extract()
            item['link'] = sel.xpath('div[@id="title"]/a/@href').extract()
            item['price'] = sel.xpath('div[@id="price"]/text()').extract()
            item['stock'] = sel.xpath('div[@id="stock"]/text()').extract()
            yield item



