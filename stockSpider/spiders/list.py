# coding=utf-8
import scrapy

from stockSpider.items import BaseInfoItem
from stockSpider.spiders.base import BaseSpider


class ListSpider(BaseSpider):
    name = 'stock_list'
    keys = ['num']
    stock_num = 'all'
    allowed_domains = []
    start_urls = []

    def __init__(self, **kwargs):
        super(ListSpider, self).__init__(**kwargs)

    def start_requests(self):
        page = 1
        url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/%s/ajax/1/' % page
        yield scrapy.Request(url, meta={'page': page}, callback=self.parse)

    def parse(self, response):
        trs = response.xpath('/html/body/table/tbody/tr')
        for tr in trs:
            info = BaseInfoItem()
            info["num"] = tr.xpath('td[2]/a/text()').extract_first()
            info["name"] = tr.xpath('td[3]/a/text()').extract_first()
            yield info
        page_info = response.xpath('//*[@class="page_info"]/text()').extract_first()
        [cur, last] = page_info.split('/')
        print page_info, cur, last
        if cur == last:
            print 'none'
        else:
            page = response.meta['page']
            page += 1
            print page
            url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/%s/ajax/1/' % page
            yield scrapy.Request(url, meta={'page': page}, callback=self.parse)