# coding=utf-8
import scrapy

from stockSpider.items import BaseInfoItem
from stockSpider.spiders.base import BaseSpider


class ListSpider(BaseSpider):
    name = 'stock_list'
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
        next_page = response.xpath('//*[@id="m-page"]/a[last()]')
        next_page_name = next_page.xpath('text()').extract_first()
        if next_page_name == '150':
            print 'none'
        else:
            page = response.meta['page']
            page += 1
            print page
            url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/%s/ajax/1/' % page
            yield scrapy.Request(url, meta={'page': page}, callback=self.parse)