# coding: utf-8
import json

import scrapy

from stockSpider.items import FinanceItem


class FinanceSpider(scrapy.Spider):
    name = "finance"
    keys = ['num']
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
        finance = FinanceItem()
        finance["name"] = name
        finance["num"] = response.meta['num']

        self.parse_subject(finance, response, 'benefit')
        self.parse_subject(finance, response, 'debt')
        self.parse_subject(finance, response, 'cash')
        self.parse_subject(finance, response, 'main')
        self.parse_subject(finance, response, 'each')
        self.parse_subject(finance, response, 'operate')
        self.parse_subject(finance, response, 'grow')
        self.parse_subject(finance, response, 'pay')

        yield finance

    def parse_subject(self, finance, response, key='benefit'):
        data = response.xpath('//*[@id="%s"]/text()' % key).extract_first()
        json_data = json.loads(data)
        names = json_data['title']
        d = json_data['simple']
        dates = d[0]
        subjects = []
        for x in range(len(dates)):
            # 每列(日期)
            date = dates[x]
            for i in range(1, len(names)):
                # 每行(科目)
                subject = {'date': date, 'name': names[i][0], 'value': d[i][x]}
                subjects.append(subject)
        finance[key] = subjects
