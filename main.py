from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings


if __name__ == '__main__':
    runner = CrawlerRunner(get_project_settings())
    # d = runner.crawl('finance', stock_num='603726', item_class='test')
    d = runner.crawl('finance', stock_num='603726')
    d.addBoth(lambda _: reactor.stop())
    reactor.run() # the script will block here until the crawling is finished