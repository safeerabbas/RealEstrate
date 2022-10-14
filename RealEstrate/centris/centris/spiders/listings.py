import scrapy
class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['www.centris.ca']

    def start_requests(self):
        pass

    def parse(self, response):
        pass
