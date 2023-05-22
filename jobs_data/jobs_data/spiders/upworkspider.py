import scrapy


class UpworkspiderSpider(scrapy.Spider):
    name = "upworkspider"
    allowed_domains = ["www.upwork.com"]
    start_urls = ["https://www.upwork.com/freelance-jobs/"]

    def parse(self, response):
        
        pass
