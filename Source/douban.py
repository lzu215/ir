import scrapy
import time


class DoubanSpider(scrapy.Spider):
    """"`What should be set in setting.py.
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                 'Version/16.1 Safari/605.1.15'
    ROBOTSTXT_OBEY = False
    FEED_EXPORT_ENCODING = 'utf-8'
    """
    name = 'douban'

    def start_requests(self):
        urls = ['https://movie.douban.com/top250?start={}&filter='.format(i) for i in range(0, 251, 25)]
        '''`test code
        url = 'https://movie.douban.com/subject/1292052/'
        yield scrapy.Request(url=url, callback=self.parse_detail)
        '''
        for url in urls:
            time.sleep(1)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        for url in response.css('div.pic a::attr(href)').getall():
            time.sleep(1)
            yield scrapy.Request(url=url, callback=self.parse_detail)

    @staticmethod
    def parse_detail(response):
        yield {
            "Title": response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first(),
            "Director": response.xpath('//*[@id="info"]/span[1]/span[2]/a//text()').extract_first(),
            "Type": response.xpath('//*[@id="info"]/span[@property="v:genre"]//text()').extract_first(),
            "Language": response.xpath('//*[@id="info"]/span[@class="pl"][3]/following::text()').extract_first(),
            "IMDB_id": response.xpath('//*[@id="info"]/span[@class="pl"][7]/following::text()').extract_first(),
            "Score": response.xpath('//*[@property="v:average"]//text()').extract_first(),
            "Rating_numbers": response.xpath('//*[@property="v:votes"]//text()').extract_first(),
            "Description": response.xpath('//*[@property="v:summary"]//text()').extract_first()
        }
