import scrapy
import json
from test4.items import MyItem
class lianjia(scrapy.spiders.Spider):
    name = "lianjia"
    allowed_domains=["bj.lianjia.com"]
    start_urls=["https://bj.lianjia.com/ershoufang/dongcheng/pg1"]
    url="https://bj.lianjia.com/ershoufang/{city}/pg{page_num}"
    page_num=1
    city_num=0
    city=['dongcheng','xicheng','chaoyang','haidian']
    def parse(self,response):
        item=MyItem()
        for each in response.xpath('//div[@class="info clear"]'):
            item['houseName']=each.xpath('div[@class="title"]/a/text()').extract()[0]
            item['housePrices']=each.xpath('div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()').extract()[0]+each.xpath('div[@class="priceInfo"]/div[@class="totalPrice"]/text()').extract()[0]
            item['houseArea']=each.xpath('div[@class="address"]/div[@class="houseInfo"]/text()').extract()[0].split("|")[1]
            item['houseUnitprice']=each.xpath('div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()').extract()[0]
            item['region']=self.city[self.city_num]
            item['pages']=self.page_num
        #print(response.body.decode())
            if(item['houseName'] and item['housePrices'] and item['houseArea'] and item['houseUnitprice']):
                yield(item)
        self.page_num+=1
        if(self.page_num==6):
            self.city_num+=1
            self.page_num=1
        new_url = self.url.format(city=self.city[self.city_num], page_num=self.page_num)
        yield scrapy.Request(url=new_url, callback=self.parse)
