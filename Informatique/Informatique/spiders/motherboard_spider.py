        # -*- coding: utf-8 -*-
import scrapy

from Informatique.items import MotherboardItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MotherboardSpider(CrawlSpider):
    name = "motherboards"
    allowed_domains = ["informatique.nl"]
    start_urls = [
        # socket 2011-3(intel)
        "http://www.informatique.nl/?m=usl&g=726&view=6&&sort=pop&pl=50",
        # socket 2011 (intel)
        "http://www.informatique.nl/?M=USL&G=670",
        # socket 1150 (intel)
        "http://www.informatique.nl/?m=usl&g=699&view=6&&sort=pop&pl=270",
        # socket 1155 (intel)
        "http://www.informatique.nl/?m=usl&g=635&view=6&&sort=pop&pl=100",
        # socket 775 (intel)
        "http://www.informatique.nl/?M=ART&G=192",
        # socket FM2+ (AMD)
        "http://www.informatique.nl/?m=usl&g=713&view=6&&sort=pop&pl=100",
        # socket AM1 (AMD) 
        "http://www.informatique.nl/?M=USL&G=717",
        # socket AM3+ (AMD)
        "http://www.informatique.nl/?m=usl&g=655&view=6&&sort=pop&pl=50",
        # socket FM1 (AMD)
        "http://www.informatique.nl/?m=usl&g=655&view=6&&sort=pop&pl=33",
        # socket FM2 (AMD)
        "http://www.informatique.nl/?M=USL&G=686",
        # onboard CPU 
        "http://www.informatique.nl/?M=USL&G=558",
        ]

    rules = (Rule(LinkExtractor(restrict_xpaths=('//*[@id="detailview"]/li/a[@class="product_overlay"]',)), callback='parse_url', follow=True), )


    def parse_url(self, response):
        for sel in response.xpath('//*[@id="product-details"]'):
            item = MotherboardItem()
            item['title'] = ''.join(sel.xpath('div/div[@id="header"]/div[@id="description"]/span/text()').extract())
            item['image'] = ''.join(sel.xpath('div/div[@id="product-panel"]/div[@id="product-image"]/a/img/@src').extract())
            item['link'] = response.url
            item['price'] = ''.join(sel.xpath('div/div[@id="product-panel"]/div[2]/div/div[@id="price"]/text()').re("\\d+,\\d+"))
            item['product_type'] = ('Moederbord')
            item['shop'] = ('Informatique')
            return item


