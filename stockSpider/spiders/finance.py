# coding: utf-8
import json

import scrapy

from stockSpider.items import FinanceItem


class FinanceSpider(scrapy.Spider):
    name = "finance"
    keys = []
    stock_num = '123456'
    item_class_name = name
    allowed_domains = []
    start_urls = []

    def __init__(self, stock_num=None, item_class="finance", **kwargs):
        super(FinanceSpider, self).__init__(**kwargs)
        self.stock_num = stock_num
        self.item_class_name = item_class

    def start_requests(self):
        url = 'http://stockpage.10jqka.com.cn/%s/finance/' % self.stock_num
        yield scrapy.Request(url, meta={'num': self.stock_num}, callback=self.parse)

    def parse(self, response):
        self.item_class_name = 'test'
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

        finance = FinanceItem()
        finance["name"] = name
        finance["num"] = response.meta['num']
        finance["benefit"] = json.loads(benefit)
        finance["debt"] = json.loads(debt)
        finance["cash"] = json.loads(cash)
        finance["main"] = json.loads(main)
        finance["each"] = json.loads(each)
        finance["operate"] = json.loads(operate)
        finance["grow"] = json.loads(grow)
        finance["pay"] = json.loads(pay)
        yield finance
