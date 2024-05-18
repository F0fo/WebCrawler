from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

class CrawlingSpider(CrawlSpider):
    name = 'mycrawler'
    allowed_domains = ['lucernefestival.ch']
    start_urls = ['https://www.lucernefestival.ch/en']

    rules = (
        Rule(LinkExtractor(allow='program/summer-festival-24')),
        Rule(LinkExtractor(allow = 'program', deny='summer-festival-24'), callback='parse_item'),
    )

    def parse_item(self, response):
        yield {
            'title': response.css('.subtitle ::text').get(),
            'location': re.sub('(\r\n)+|(\xa0)+|(\n)+|(\t)',' ', ''.join(response.css('.medium-9 p::text ').getall()[-3:])), #Must update to give a location to conerts in the streets
            'date_time': re.sub('(\n)+|(\t)+','',''.join(response.css('.subtitle ::text').getall()[3].split('|')[:2])),
            'artist': list(filter(lambda isempty: len(isempty) > 0,map(lambda remove: re.sub('(\n)+|(\t)+|(  +)', '', remove), response.css('.performers-list ::text').getall())))[1:],
            'works': list(filter(lambda isempty: len(isempty) > 0,map(lambda remove: re.sub('(\n)+|(\t)+|(  +) |(\r)+ | (\xa0)+', '', remove), response.css('.cell .medium-9 ::text').getall())))[:-6],
            'image_link': 'www.lucernefestival.ch' + response.xpath('//picture').get().split('<img src=')[1].lstrip().split(' ')[0][1:-1]

,
        }


