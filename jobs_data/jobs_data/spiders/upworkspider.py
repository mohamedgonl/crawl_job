import scrapy
from urllib.parse import urlencode
API_KEY = 'bb3dd64e-91dd-48a4-8fea-44348e813d5a'

def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class UpworkSpider(scrapy.Spider):
    name = "upwork"
    allowed_domains = ["www.upwork.com"]
    
    domain = "https://www.upwork.com"
    
    def start_requests(self):
           
        urls = [
            "/freelance-jobs/3d-visualizations/"
        ]
        for url in urls:
            yield scrapy.Request(url=get_scrapeops_url(self.domain + url), callback=self.get_job,) 

    def parse(self, response):  
        job_type = response.css("#main > div > div > section.links-wrapper-section.vs-bg-white.pb-30.pb-md-50.pb-xl-80 > div > div > div > div > div.col-lg-9 > section > div > ul > div > a ")
        for job in job_type:
            job_type_url =self.domain+ job.attrib['href']
            job_name = job.attrib['title']
            yield scrapy.Request(url=get_scrapeops_url(self.domain + job_type_url), callback=self.get_job, cb_kwargs={'job_type' : job_name})
            break

    
    def get_job(self, response):
        print("----------------------------------------GET JOB ----------------------------------")
        print(response.css("#main > div > div > div:nth-child(3) > section.job-grid.vs-bg-white > div.container-visitor > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section > div.job-tile-content > div.mb-20 > a"))
        pass
    
    
    
    #main > div > div > div:nth-child(3) > section.job-grid.vs-bg-white > div.container-visitor > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > section > div.job-tile-content > div.mb-20 > a
        
        

