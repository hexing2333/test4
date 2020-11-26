# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):
    name=scrapy.Field()
    location_1=scrapy.Field()
    location_2=scrapy.Field()
    location_3=scrapy.Field()
    area=scrapy.Field()
    kind=scrapy.Field()
    unitprice=scrapy.Field()
    allprice=scrapy.Field()