# gotten from https://www.dol.gov/general/jobs/interview-tips

from pathlib import Path

import scrapy

class interviewTipsSpider(scrapy.Spider):
    name = "interview-one"
    
    def start_requests(self):
        urls=[
            "https://www.dol.gov/general/jobs/interview-tips/"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        filename = "interview-one-web.txt"
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')        