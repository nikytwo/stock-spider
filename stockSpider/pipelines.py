# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

from scrapy.exceptions import DropItem


class MultItemPipeline(object):
    def process_item(self, item, spider):
        spider.stock_num = item['num']
        return item


class CoverPipeline(object):
    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        file_path = '%s/%s.json' % (spider.name, spider.stock_num)
        if os.path.exists(file_path):
            os.remove(file_path)


class UnDuplicatedPipeline(object):
    item_ids = set()

    def process_item(self, item, spider):
        if self.contains(item, spider.keys):
            raise DropItem("item is existed, id: %s" % self.get_id(item, spider.keys))
        else:
            return item

    def open_spider(self, spider):
        keys = spider.keys
        file_path = '%s/%s.json' % (spider.name, spider.stock_num)
        if not os.path.exists(file_path):
            return

        file = open(file_path)
        for line in file:
            item_json = json.loads(line)
            id = self.get_id(item_json, keys)
            self.item_ids.add(id)

    def contains(self, item, keys):
        id = self.get_id(item, keys)
        if self.item_ids.__contains__(id):
            return True
        return False

    def get_id(self, item, keys):
        id = ""
        for key in keys:
            id += "#" + item[key]
        return id