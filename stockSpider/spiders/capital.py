
import scrapy
from scrapy.spiders import BaseSpider

from stockSpider.items import CapitalItem


class CapitalSpider(BaseSpider):
    name = 'capital'
    allowed_domains = []
    start_urls = []

    def __init__(self, stock_num='002741', **kwargs):
        super(CapitalSpider, self).__init__(**kwargs)
        self.stock_num = stock_num

    def start_requests(self):
        url = 'http://stockpage.10jqka.com.cn/%s/holder/' % self.stock_num
        yield scrapy.Request(url, meta={'num': self.stock_num}, callback=self.parse)

    def parse(self, response):
        name = response.xpath('//*[@id="in_squote"]/div/h1/a[1]/strong/text()').extract_first()
        date_list = response.xpath('//*[@id="stockcapit"]/div[2]/table/thead/tr/th')
        cap_list = response.xpath('//*[@id="stockcapit"]/div[2]/table/tbody/tr[1]/td')
        print date_list
        for i in range(len(cap_list)):
            print cap_list[i]
            print date_list[i + 1]
            capital = CapitalItem()
            capital['name'] = name
            capital['num'] = response.meta['num']
            capital['date'] = date_list[i + 1].xpath('text()').extract_first()
            capital['count'] = cap_list[i].xpath('text()').extract_first()
            yield capital
