# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):
    pages=scrapy.Field()
    region=scrapy.Field()
    houseName=scrapy.Field()
    housePrices=scrapy.Field()
    houseArea=scrapy.Field()
    houseUnitprice=scrapy.Field()