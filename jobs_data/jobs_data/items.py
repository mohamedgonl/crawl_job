# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Job(scrapy.Item):
    name = scrapy.Field()
    posting_date = scrapy.Field()
    salary = scrapy.Field()
    hours = scrapy.Field()
    closing_date = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    job_type = scrapy.Field()
    job_reference = scrapy.Field()
    
    
