import scrapy
class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['www.centris.ca']
    start_urls = ['http://www.centris.ca/']

    def parse(self, response):
        pass
