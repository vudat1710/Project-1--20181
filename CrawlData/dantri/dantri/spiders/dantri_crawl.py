from scrapy import Spider
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class DantriCrawlSpider(CrawlSpider):
    name = "dantri_crawl"
    allowed_domains = ['dantri.com.vn']
    start_urls = ['https://dantri.com.vn/nhip-song-tre.htm',]
    COUNT_MAX = 1000
    count = 0
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="html"]/body/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/a')),
        callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        urls = response.xpath('//div[@class="mr1"]/a/@href')
        for url in urls:
            self.count = self.count + 1
            if (self.count < self.COUNT_MAX):
                connect_to_url = response.urljoin(url.extract())
                yield Request(connect_to_url, callback=self.parse_question)

    def parse_question(self, response):
        title = response.xpath('//*[@id="ctl00_IDContent_ctl00_divContent"]/h1/text()').extract()
        span = response.xpath('//*[@id="ctl00_IDContent_ctl00_divContent"]/h2/text()').extract()
        contents = response.xpath('//*[@id="divNewsContent"]/p/text()').extract()
        str2 = ''.join(title)
        str3 = ''.join(span)
        f = open("data2.txt","a")
        f.write(str2.strip())
        f.write('. ')
        f.write(str3.strip())
        f.write(' ')
        for content in contents:
            str1 = ''.join(content)
            if (str1 == 'Theo ' or str1 == 'Theo'):
                str1 = ''
            f.write(str1.strip())
            f.write(' ')
        f.write('\n')
        f.close()


    

    
