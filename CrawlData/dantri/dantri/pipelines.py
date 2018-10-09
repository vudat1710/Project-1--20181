# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import (
    create_engine,
    Table,
    Column,
    MetaData,
    Integer,
    Text,
    select
)
from scrapy.exceptions import DropItem
import string

class DantriPipeline(object):
    def process_item(self, item, spider):
        is_valid = True
        for data in item:
            if not data:
                is_valid = False
                raise DropItem("Missing %s" %data)
        if is_valid:
            obj = open("ahihi.txt", "wb")
            title = ''.join(item['title']).encode('utf-8')
            content = ''.join(item['content']).encode('utf-8')
            obj.write(title)
            obj.write('\n')
            obj.write(content)
            obj.write('\n')
            obj.close()
        return item
