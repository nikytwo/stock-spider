
import scrapy


class CapitalSpider(scrapy.Spider):
    name = 'capital'
    allowed_domains = []
    start_urls = []

    def __init__(self, stock_num='002741', **kwargs):
        super(CapitalSpider, self).__init__(**kwargs)
        self.stock_num = stock_num

    def start_requests(self):
        url = 'http://stockpage.10jqka.com.cn/%s/holder/' % self.stock_num
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        pass