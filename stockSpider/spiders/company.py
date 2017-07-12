
#

import scrapy

from stockSpider.items import CompanyItem
from stockSpider.spiders.base import BaseSpider


class CompanySpider(BaseSpider):
    name = 'company'
    allowed_domains = []
    start_urls = []

    def __init__(self, stock_num='002741', **kwargs):
        super(CompanySpider, self).__init__(**kwargs)
        self.stock_num = stock_num

    def start_requests(self):
        url = 'http://stockpage.10jqka.com.cn/%s/company/' % self.stock_num
        yield scrapy.Request(url, meta={'num': self.stock_num}, callback=self.parse)

    def parse(self, response):
        company_name = response.xpath('//*[@id="detail"]/div[2]/table/tbody/tr[1]/td[2]/span/text()').extract_first()
        vocation = response.xpath('//*[@id="detail"]/div[2]/table/tbody/tr[2]/td[2]/span/text()').extract_first()
        province = response.xpath('//*[@id="detail"]/div[2]/table/tbody/tr[1]/td[3]/span/text()').extract_first()
        start_date = response.xpath('//*[@id="publish"]/div[2]/table/tr[2]/td[1]/span/text()').extract_first()
        web_home = response.xpath('//*[@id="detail"]/div[2]/table/tbody/tr[3]/td[2]/span/a/text()').extract_first()

        company = CompanyItem()
        company['num'] = response.meta['num']
        company['company_name'] = company_name
        company['province'] = province
        company['vocation'] = vocation
        company['web_home'] = web_home
        company['start_date'] = start_date
        yield company
