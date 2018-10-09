# -*- coding: utf-8 -*-
# from scrapy import Selector
from scrapy import Spider
from scrapy import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 
from scrapy.contrib.spiders import CrawlSpider, Rule

class DantriCrawlSpider(CrawlSpider):
    name = "dantri_crawl"
    allowed_domains = ['dantri.com.vn']
    start_urls = ['https://dantri.com.vn/phap-luat.htm',]
    urls = []
    COUNT_MAX = 10000
    count = 0
    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('/html/body/form/div[6]/div[1]/div[1]/div[1]/div[4]/div[1]/a')),
        callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        urls1 = response.xpath('//div[@class="mr1"]/a/@href')
        for url1 in urls1:
            # full_url = url.extract()
            self.count = self.count + 1
            if (self.count < self.COUNT_MAX):
                connect_to_url = response.urljoin(url1.extract())
                yield Request(connect_to_url, callback=self.parse_question)

    def parse_question(self, response):
        title = response.xpath('/html/body/form/div[9]/div[3]/div/div[1]/div[1]/div[1]/h1/text()').extract()
        span = response.xpath('/html/body/form/div[9]/div[3]/div/div[1]/div[1]/div[1]/h2/text()').extract()
        contents = response.xpath('//*[@id="divNewsContent"]/p/text()').extract()
        str2 = ''.join(title).encode('utf-8')
        str3 = ''.join(span).encode('utf-8')
        f = open("data.txt","a")
        f.write(str2)
        f.write('\n')
        f.write(str3)
        for content in contents:
            str1 = ''.join(content).encode('utf-8')
            if (str1 == 'Theo ' or str1 == 'Theo'):
                str1 = ''
            f.write(str1)
        f.write('\n')
        f.close()


    

    
