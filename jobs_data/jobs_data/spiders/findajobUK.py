import scrapy
from jobs_data.items import Job

class FindajobukSpider(scrapy.Spider):
    name = "findajobUK"
    allowed_domains = ["findajob.dwp.gov.uk"]
    start_urls = ["https://findajob.dwp.gov.uk/search?loc=86383&pp=50"]

    def parse(self, response):
        jobs_detail = response.css(".search-result .govuk-link")
        for detail in jobs_detail:
            detail_page = detail.attrib['href']
            yield response.follow(detail_page, callback = self.get_detail)
        
        next_page = response.css(" .pager-next").attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
            
             
    def get_detail(self, response): 
        job = Job()
        detail = response.css(".govuk-table__cell::text").getall()
        
        job['name'] = response.css(".govuk-heading-l::text").get().replace('\n','').replace(' ','')
        job["posting_date"] = detail[0].replace('\n','').replace(' ','')
        job['salary'] = detail[1].replace('\n','').replace(' ','')
        job['hours'] = detail[2].replace('\n','').replace(' ','')
        job['closing_date']= detail[3].replace('\n','').replace(' ','')
        job['location'] = detail[4].replace('\n','').replace(' ','')
        job['company'] = detail[5].replace('\n','').replace(' ','')
        job['job_type'] = detail[6].replace('\n','').replace(' ','')
        job['job_reference'] = detail[7].replace('\n','').replace(' ','')
        
        yield job
