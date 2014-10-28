# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CasesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()



class PowerSupplyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()



class MotherboardItem(scrapy.Item):
	# generic for different sockets, just different starting links
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()


class FanItem(scrapy.Item):
    # generic for different sockets, just different starting links
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()


class SoundcardItem(scrapy.Item):
    # generic for different sockets, just different starting links
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()



class harddiskItem(scrapy.Item):
    # generic for different sockets, just different starting links
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
