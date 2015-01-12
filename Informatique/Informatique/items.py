# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#Informatique
class CasesItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()

class PowerSupplyItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()

class MotherboardItem(scrapy.Item):
	# generic for different motherboards, just different starting links
    title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    socket = scrapy.Field()
    ddr = scrapy.Field()

class FanItem(scrapy.Item):
    # generic for different fans, just different starting links
    title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()

class SoundcardItem(scrapy.Item):
    # generic for different soundcards, just different starting links
    title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()

class harddiskItem(scrapy.Item):
    # generic for different harddisks, just different starting links
    title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()

class RamddrItem(scrapy.Item):
    # generic for different ddr ram modules, just different starting links
    title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()