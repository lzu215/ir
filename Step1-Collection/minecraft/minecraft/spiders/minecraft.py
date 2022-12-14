import scrapy
import time


class MinecraftSpider(scrapy.Spider):
    """"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                 'Version/16.1 Safari/605.1.15'
    ROBOTSTXT_OBEY = False
    FEED_EXPORT_ENCODING = 'utf-8'
    ITEM_PIPELINES = {
        'minecraft.pipelines.MinecraftPipeline': 300,
    }
    """
    name = 'minecraft'

    def start_requests(self):
        urls = ['https://www.planetminecraft.com/mods/?p={}'.format(i) for i in range(1, 101)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        # url = 'https://www.planetminecraft.com/mod/hypixel-skyblockplus-renew/'
        # yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse(self, response, *args, **kwargs):
        for url in response.css('div.r-preview a::attr(href)').getall():
            time.sleep(1)
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_detail)

    @staticmethod
    def parse_detail(response):
        yield {
            "Title": response.xpath('//*[@id="resource-title-text"]/h1/text()').extract_first(),
            "Description": response.xpath('//*[@id="r-text-block"]//text()').extract(),
            "Published time": response.xpath('//*[@id="resource-info"]/div/span/@title').extract_first(),
            "Views": response.xpath('//*[@id="resource-info"]/ul/li[1]/span[1]/text()').extract_first(),
            "Downloads": response.xpath('//*[@id="resource-info"]/ul/li[2]/span[1]/text()').extract_first(),
            "Credit": response.xpath('//*[@id="resource_object"]/table//*[text()[contains(.,\'Credit\')]]/../td[2]//text()').extract_first(),
            "Progress": response.xpath('//*[@id="resource_object"]/table//*[text()[contains(.,\'Progress\')]]/../td[2]//text()').extract_first(),
            "Game Version": response.xpath('//*[@id="resource_object"]/table//*[text()[contains(.,\'Game Version\')]]/../td[2]//text()').extract_first(),
            "Tags": response.xpath('//*[@id="item_tags"]//text()').extract(),
            "Url": response.url
        }
