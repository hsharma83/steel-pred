# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SmintItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    #description = scrapy.Field()
    date = scrapy.Field()
    #category = scrapy.Field()

class SteelorbisItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()

class MetaljunctionItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    #content = scrapy.Field()
