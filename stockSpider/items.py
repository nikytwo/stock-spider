# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    benefit = scrapy.Field()
    debt = scrapy.Field()
    cash = scrapy.Field()
    main = scrapy.Field()
    each = scrapy.Field()
    operate = scrapy.Field()
    grow = scrapy.Field()
    pay = scrapy.Field()
    pass
