# coding=utf-8
# http://d.10jqka.com.cn/v2/line/hs_002741/02/2016.js # 后复权
# http://d.10jqka.com.cn/v2/line/hs_002741/01/2016.js # 前复权
# http://d.10jqka.com.cn/v2/line/hs_002741/00/2016.js # 不复权

import scrapy


class HistoryPriceSpider(scrapy.Spider):
    name = 'history'
    allowed_domains = []
    start_urls = []

    def __init__(self, stock_num='002741', **kwargs):
        super(HistoryPriceSpider, self).__init__(**kwargs)
        self.stock_num = stock_num

    def start_requests(self):
        url = 'http://d.10jqka.com.cn/v2/line/hs_%s/01/2016.js' % self.stock_num
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        pass