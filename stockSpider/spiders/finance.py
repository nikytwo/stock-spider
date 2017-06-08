# coding: utf-8
import json

import scrapy

from stockSpider.items import StockspiderItem


class FinanceSpider(scrapy.Spider):
    name = "finance"
    allowed_domains = []
    start_urls = ['http://stockpage.10jqka.com.cn/603199/finance/']

    def parse(self, response):
        name = response.xpath('//*[@id="in_squote"]/div/h1/a[1]/strong/text()').extract_first()
        print name
        benefit = response.xpath('//*[@id="benefit"]/text()').extract_first()
        debt = response.xpath('//*[@id="debt"]/text()').extract_first()
        cash = response.xpath('//*[@id="cash"]/text()').extract_first()
        main = response.xpath('//*[@id="main"]/text()').extract_first()
        each = response.xpath('//*[@id="each"]/text()').extract_first()
        operate = response.xpath('//*[@id="operate"]/text()').extract_first()
        grow = response.xpath('//*[@id="grow"]/text()').extract_first()
        pay = response.xpath('//*[@id="pay"]/text()').extract_first()

        finance = StockspiderItem()
        finance["name"] = name
        finance["benefit"] = json.loads(benefit)
        finance["debt"] = json.loads(debt)
        finance["cash"] = json.loads(cash)
        finance["main"] = json.loads(main)
        finance["each"] = json.loads(each)
        finance["operate"] = json.loads(operate)
        finance["grow"] = json.loads(grow)
        finance["pay"] = json.loads(pay)
        yield finance