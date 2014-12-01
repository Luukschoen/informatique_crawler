        # -*- coding: utf-8 -*-
import scrapy

from project.items import MotherboardItem

class MotherboardSpider(scrapy.Spider):
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

    def parse(self, response):
        for sel in response.xpath('//div/div/div[@id="content"]/ul/li'):
            item = MotherboardItem()
            item['title'] = sel.xpath('div[@id="title"]/a/text()').extract()
            item['link'] = sel.xpath('div[@id="title"]/a/@href').extract()
            item['price'] = sel.xpath('div[@id="price"]/text()').extract()
            item['stock'] = sel.xpath('div[@id="stock"]/text()').extract()
            yield item



