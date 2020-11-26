# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import csv
import test4.DataProcess
from test4.DataProcess import Process
class Mypipeline(object):
    def __init__(self):
        self.file = open('MyData.csv', 'w', encoding='utf-8-sig',newline="")
        self.fieldnames = ["name", "location_1", "location_2", "location_3","kind","area","unitprice","allprice"]
        self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        # 写入第一行字段名，因为只要写入一次，所以文件放在__init__里面
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self,spider):
        self.file.close()
        Process()

