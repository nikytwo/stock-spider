import scrapy


class BaseSpider(scrapy.Spider):
    name = "base"
    stock_num = '123456'

    def __init__(self, **kwargs):
        super(BaseSpider, self).__init__(**kwargs)