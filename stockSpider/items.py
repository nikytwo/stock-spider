# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    name = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field()
    sold = scrapy.Field()


class BaseInfoItem(scrapy.Item):
    name = scrapy.Field()
    num = scrapy.Field()


class CompanyItem(BaseInfoItem):
    company_name = scrapy.Field()
    vocation = scrapy.Field()
    province = scrapy.Field()
    web_home = scrapy.Field()
    start_date = scrapy.Field()


class FinanceItem(BaseInfoItem):
    # define the fields for your item here like:
    benefit = scrapy.Field()
    debt = scrapy.Field()
    cash = scrapy.Field()
    # main = scrapy.Field()
    # each = scrapy.Field()
    # operate = scrapy.Field()
    # grow = scrapy.Field()
    # pay = scrapy.Field()
    pass


class CapitalItem(BaseInfoItem):
    date = scrapy.Field()
    count = scrapy.Field()


class HistoryPriceItem(BaseInfoItem):
    date = scrapy.Field()
    start_price = scrapy.Field()
    max_price = scrapy.Field()
    min_price = scrapy.Field()
    end_price = scrapy.Field()
    total_count = scrapy.Field()
    total_price = scrapy.Field()
    change_rate = scrapy.Field()


if __name__ == '__main__':
    stock_count = 0.9472
    # pe = 18.0
    price = 35.41
    rad_year = 0.25
    in_per_last = 0.77
    in_per = (in_per_last*(1+rad_year)) # price / pe
    years = 10
    total_price = stock_count * price

    print total_price
    print "pe0=", price/in_per_last
    print "pe1=", price/(0.35*(in_per_last/0.14))
    print "pe2=", price/(in_per_last*(1+rad_year))

    for i in range(years):
        if i > 0:
            in_per = in_per * (1 + rad_year)
        price = price + in_per
        print i, price, in_per, price / in_per

    # print price
