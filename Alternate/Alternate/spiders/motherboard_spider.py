# -*- coding: utf-8 -*-
import scrapy

from Alternate.items import MotherboardItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor




class MotherboardSpider(CrawlSpider):
    name = 'motherboards'
    allowed_domains = ["alternate.nl"]
    start_urls = [
        #INTEL
        "http://www.alternate.nl/html/product/listing.html?navId=11626&tk=7&lk=9435",
        #AMD
        "http://www.alternate.nl/html/product/listing.html?navId=11622&tk=7&lk=9419",
        # "http://www.alternate.nl/html/product/listing.html?navId=1386&tk=7&lk=9439",
        # "http://www.alternate.nl/html/product/listing.html?navId=17509&tk=7&lk=9450",
        # "http://www.alternate.nl/html/product/listing.html?navId=10652&tk=7&lk=9446",
        # "http://www.alternate.nl/html/product/listing.html?navId=14536&tk=7&lk=9448",
        # "http://www.alternate.nl/html/product/listing.html?navId=20673&tk=7&lk=13777",
        # "http://www.alternate.nl/html/product/listing.html?navId=19688&tk=7&lk=11638",
        # "http://www.alternate.nl/html/product/listing.html?navId=1376&tk=7&lk=9427",
        # "http://www.alternate.nl/html/product/listing.html?navId=11942&tk=7&lk=9432",
        # "http://www.alternate.nl/html/product/listing.html?navId=16053&tk=7&lk=9434",
        # "http://www.alternate.nl/html/product/listing.html?navId=18661&tk=7&lk=10303",
        # "http://www.alternate.nl/html/product/listing.html?navId=9020&tk=7&lk=9428",
        ]

    rules = (Rule(LinkExtractor(restrict_xpaths=('//div[@class="listRow"]/a',)), callback='parse_url', follow=True), )

    def parse_url(self, response):
        for sel in response.xpath('//*[@id="buyProduct"]'):
            item = MotherboardItem()
            item['title'] = ''.join(sel.xpath('div[1]/h1/span[2]/text()').extract())
            base_url = "http://www.alternate.nl"
            image_url = base_url + sel.xpath('div[@class="productPics"]/div/span[@class="picture"]/img/@src').extract()[0]
            item['image'] = ''.join(image_url)
            item['link'] = response.url
            item['price'] = ''.join(sel.xpath('div[@class="productShort"]/div[@class="price"]/span[@itemprop="price"]/text()').re("\\d+"))
            item['socket'] = ''.join(sel.xpath('div[@class="productDetailsBox"]/div[@class="content"]/div[@class="details"]/div[@class="moreInfos"]/div[@class="techData"]/table/tr[1]/td[2]/text()').extract())
            item['type'] = ''.join(sel.xpath('div[@class="productDetailsBox"]/div[@class="content"]/div[@class="details"]/div[@class="moreInfos"]/div[@class="techData"]/table/tr[13]/td[3]/text()').extract())
            item['product_type'] = ('Moederbord')
            item['shop'] = ('Alternate')
            return item





