
#

import scrapy

from stockSpider.spiders.base import BaseSpider


class CompanySpider(BaseSpider):
    name = 'company'
    allowed_domains = []
    start_urls = []

    def __init__(self, stock_num='002741', **kwargs):
        super(CompanySpider, self).__init__(**kwargs)
        self.stock_num = stock_num

    def start_requests(self):
        # url = 'http://www.iwencai.com/stockpick/search?tid=stockpick&qs=stockpick_diag&ts=1&w=%s' % self.stock_num
        url = 'http://stockpage.10jqka.com.cn/%s/company/' % self.stock_num
        yield scrapy.Request(url, meta={'num': self.stock_num}, callback=self.parse)

    def parse(self, response):
        company_name = response.xpath('//*[@id="detail"]/div[2]/table/tbody/tr[1]/td[2]/span/text()').extract_first()
        vocation_list = response.xpath('//*[@id="detail"]/div[2]/table/tbody/tr[2]/td[2]/span')
        province = response.xpath('//*[@id="detail"]/div[2]/table/tbody/tr[1]/td[3]/span')
        start_date = response.xpath('//*[@id="publish"]/div[2]/table/tr[2]/td[1]/span')
        print response.meta['num']
        print company_name
        print province.xpath('text()').extract_first()
        print vocation_list.xpath('text()').extract_first()
        print start_date.xpath('text()').extract_first()
        # for i in range(len(cap_list)):
        #     print cap_list[i]
        #     print date_list[i + 1]
        #     capital = CapitalItem()
        #     capital['name'] = name
        #     capital['num'] = response.meta['num']
        #     capital['date'] = date_list[i + 1].xpath('text()').extract_first()
        #     capital['count'] = cap_list[i].xpath('text()').extract_first()
        #     yield capital
