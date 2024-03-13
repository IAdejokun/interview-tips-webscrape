# gotten from https://ung.edu/career-services/online-career-resources/interview-well/tips-for-a-successful-interview.php

from pathlib import Path

import scrapy

class interviewTipsSpider(scrapy.Spider):
    name = "interview-Two"
    
    def start_requests(self):
        urls=[
            "https://ung.edu/career-services/online-career-resources/interview-well/tips-for-a-successful-interview.php"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        filename = "interview-two-web.txt"
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')        