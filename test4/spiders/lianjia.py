import scrapy
import json
from test4.items import MyItem
class lianjia(scrapy.spiders.Spider):
    name = "lianjia"
    allowed_domains=["bj.fang.lianjia.com"]
    start_urls=["https://bj.fang.lianjia.com/loupan/pg1/"]
    url="https://bj.fang.lianjia.com/loupan/pg{page_num}/"
    page_num=1
    def parse(self,response):
        item=MyItem()
        for each in response.xpath('//div[@class="resblock-desc-wrapper"]'):
            price=""
            price_kind=""
            if(each.xpath('div[@class="resblock-name"]/a/text()')):
                item['name']=each.xpath('div[@class="resblock-name"]/a/text()').extract()[0]
            if(each.xpath('div[@class="resblock-location"]/span[1]/text()')):
                item['location_1']=each.xpath('div[@class="resblock-location"]/span[1]/text()').extract()[0]
            if(each.xpath('div[@class="resblock-location"]/span[2]/text()')):
                item['location_2']=each.xpath('div[@class="resblock-location"]/span[2]/text()').extract()[0]
            if(each.xpath('div[@class="resblock-location"]/a/text()')):
                item['location_3']=each.xpath('div[@class="resblock-location"]/a/text()').extract()[0]
            if(each.xpath('a[@class="resblock-room"]/span[1]/text()')):
                item['kind']=each.xpath('a[@class="resblock-room"]/span[1]/text()').extract()[0]
            if(each.xpath('div[@class="resblock-area"]/span/text()')):
                item['area']=each.xpath('div[@class="resblock-area"]/span/text()').extract()[0]
            if(each.xpath('div[@class="resblock-price"]/div[@class="main-price"]/span[1]/text()')):
                price=each.xpath('div[@class="resblock-price"]/div[@class="main-price"]/span[1]/text()').extract()[0]
            if(each.xpath('div[@class="resblock-price"]/div[@class="main-price"]/span[2]/text()')):
                price_kind=each.xpath('div[@class="resblock-price"]/div[@class="main-price"]/span[2]/text()').extract()[0]
                if(price_kind==" 元/㎡(均价)"):
                    item['unitprice']=price
                    item['allprice']=""
                elif(price_kind==" 万/套(总价)"):
                    item['allprice']=price
                    item['unitprice']=""

            yield(item)
        self.page_num+=1
        if(self.page_num<=19):
            new_url = self.url.format(page_num=self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)
