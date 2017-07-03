# coding=utf-8
import csv

import scrapy

from stockSpider.items import HouseItem


class HouseSpider(scrapy.Spider):
    name = "house"
    stock_num = 'tingtao2-4n13-15-sold'
    item_class_name = name
    allowed_domains = []
    start_urls = []

    def start_requests(self):
        # url = 'http://house.shunde.gov.cn/dy_list.jsp?id=2017010603&type=-1'
        url = 'http://house.shunde.gov.cn/dy_list.jsp?id=2017010003&type=-1'
        # name = 'test'
        # url = 'http://house.shunde.gov.cn/dy_detailinfo.jsp?id=201701000783'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        elemList = response.xpath('//*/td[@id]')
        for elem in elemList:
            name = elem.xpath('a/text()').extract_first()
            if not name:
                continue
            link = elem.xpath('a/@href').extract_first()
            sale_status = elem.xpath('@class').extract_first()
            if sale_status == 'status_0':
                sold = False
            else:
                sold = True
            url = 'http://house.shunde.gov.cn/%s' % link
            print name, url, sold, sale_status

            house = HouseItem()
            house['name'] = name
            house['sold'] = sold
            yield house
            # yield scrapy.Request(url=url, meta={'name': name, 'sold': sold}, callback=self.parse_link)


    def parse_link(self, response):
        house = HouseItem()
        name = response.meta['name']
        size = response.xpath('//*[@class="detail_table detail_table22"]/tbody/tr[4]/td[2]/text()').extract_first().replace('\t', '').replace('\r\n', '')
        price = response.xpath('//*[@class="detail_table detail_table22"]/tbody/tr[7]/td[2]/div[1]/text()').extract_first().replace('\t', '')
        print  size, price
        house['name'] = name
        house['size'] = size
        house['price'] = price
        house['sold'] = response.meta['sold']
        yield house

if __name__ == "__main__":
    """
    更新销售情况
    """
    sold_reader = csv.reader(open('../../house/tingtao2-4n13-15-sold.csv'))

    sold_house = {}
    for row in sold_reader:
        sold_house[row[0]] = row[1]
    # print sold_house

    reader = csv.reader(open('../../house/tingtao2-4n13-15.csv'))
    out = open('../../house/tingtao2-4n13-15-test.csv', 'wb')
    for row in reader:
        row.append(sold_house[row[0]])
        # print row
        csv_writer = csv.writer(out, dialect='excel')
        csv_writer.writerow(row)


