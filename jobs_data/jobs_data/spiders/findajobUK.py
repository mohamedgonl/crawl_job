import scrapy

class FindajobukSpider(scrapy.Spider):
    name = "findajobUK"
    allowed_domains = ["findajob.dwp.gov.uk"]
    start_urls = ["https://findajob.dwp.gov.uk/search?loc=86383&pp=50"]
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self.parse)
    
    def parse(self, response):
        job_types_href = response.css("#main > main > div.govuk-grid-row > div.govuk-grid-column-one-quarter.column-filters > ul:nth-child(11) > li > a")
        job_types = response.css("#main > main > div.govuk-grid-row > div.govuk-grid-column-one-quarter.column-filters > ul:nth-child(11) > li > a ::text")
        for (href, type) in zip(job_types_href, job_types):
            yield response.follow(href.attrib['href'], callback=self.get_job, cb_kwargs={'job_type': type.get().replace('\n', '').strip()})


    def get_job(self, response, job_type):
        jobs_detail = response.css("#search_results > div > h3 > a")
        for detail in jobs_detail:
            detail_page = detail.attrib['href']
            yield response.follow(detail_page, callback = self.get_detail,cb_kwargs={'job_type': job_type} )
        
        next_page = response.css("#pager > div > a").attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback = self.get_detail ,cb_kwargs={'job_type': job_type})
            
             
    def get_detail(self, response, job_type): 
        job_name = response.xpath("/html/body/div[5]/main/div[2]/div[1]/h1/text()").get().replace('\n', '').strip()
        job = {'job_type': job_type, 'job_name' : job_name}
        
        rows_detail_job = response.css("#ad_details > div.govuk-grid-column-two-thirds > table > tbody > tr")
        for row in rows_detail_job:
            row_name = row.css('th::text').get().replace('\n', '').strip().lower().replace(' ', '_')
            row_value = row.css('td::text').get().replace('\n', '').strip()
            job[row_name] = row_value
        yield job
