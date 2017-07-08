import scrapy


class BaseSpider(scrapy.Spider):
    name = "base"
    keys = ['num']
    stock_num = '123456'

    def __init__(self, **kwargs):
        super(BaseSpider, self).__init__(**kwargs)