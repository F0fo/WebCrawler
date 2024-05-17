from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = 'mycrawler'
    allowed_domains = ['lucernefestival.ch']
    start_urls = ['https://www.lucernefestival.ch/en']

    rules = (
        Rule(LinkExtractor(allow='en/program')),
    )

