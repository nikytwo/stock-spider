import json
import os

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.project import get_project_settings

from stockSpider.items import BaseInfoItem
from stockSpider.spiders.finance import FinanceSpider

if __name__ == '__main__':


    # file_path = '%s/%s.json' % ('stock_list', 'all')
    # if os.path.exists(file_path):
    #     file = open(file_path)
    #     for line in file:
    #         info = json.loads(line)
    #         num = info['num']
    #         print num

    # runner = CrawlerRunner(get_project_settings())
    # # d = runner.crawl('finance', stock_num='603726', item_class='test')
    # d = runner.crawl('history', stock_num=num)
    # d.addBoth(lambda _: reactor.stop())
    # reactor.run() # the script will block here until the crawling is finished

    settings = get_project_settings()
    list = ['600569','300686']
    process = CrawlerProcess(settings=settings)
    process.crawl('history', num_list=list)
    process.start()