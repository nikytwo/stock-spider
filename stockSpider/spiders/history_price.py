# coding=utf-8
# http://d.10jqka.com.cn/v2/line/hs_002741/02/2016.js # 后复权
# http://d.10jqka.com.cn/v2/line/hs_002741/01/2016.js # 前复权
# http://d.10jqka.com.cn/v2/line/hs_002741/00/2016.js # 不复权
import json

import scrapy

from stockSpider.items import HistoryPriceItem


class HistoryPriceSpider(scrapy.Spider):
    name = 'history'
    keys = ['num', 'date']
    allowed_domains = []
    start_urls = []

    def __init__(self, stock_num='002741', year=2017, **kwargs):
        super(HistoryPriceSpider, self).__init__(**kwargs)
        self.stock_num = stock_num
        self.year = year

    def start_requests(self):
        url = 'http://d.10jqka.com.cn/v2/line/hs_%s/01/%s.js' % (self.stock_num, self.year)
        yield scrapy.Request(url, meta={'num': self.stock_num}, callback=self.parse)

    def parse(self, response):
        num = response.meta['num']
        data = response.body_as_unicode()
        start = data.index('{')
        data = data[start : -1]
        json_obj = json.loads(data)
        his_list = json_obj['data'].split(';')
        for his in his_list:
            elems = his.split(',')
            history = HistoryPriceItem()
            history['num'] = num
            history['date'] = elems[0]
            history['start_price'] = elems[1]
            history['max_price'] = elems[2]
            history['min_price'] = elems[3]
            history['end_price'] = elems[4]
            history['total_count'] = elems[5]
            history['total_price'] = elems[6]
            history['change_rate'] = elems[7]
            yield history
