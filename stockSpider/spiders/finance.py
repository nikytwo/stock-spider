# coding: utf-8

import scrapy

from stockSpider.items import StockspiderItem


class FinanceSpider(scrapy.Spider):
    name = "finance"
    allowed_domains = []
    start_urls = ['http://stockpage.10jqka.com.cn/603199/finance/']

    def parse(self, response):
        name = response.xpath('//*[@id="in_squote"]/div/h1/a[1]/strong/text()').extract_first()
        print name

        finance = StockspiderItem()
        finance["name"] = name
        yield finance