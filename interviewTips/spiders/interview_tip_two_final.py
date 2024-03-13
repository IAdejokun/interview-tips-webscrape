import scrapy


class interviewTipsSpider(scrapy.Spider):
    name = "interview-two-final"
    
    start_urls=[
            "https://ung.edu/career-services/online-career-resources/interview-well/tips-for-a-successful-interview.php"
        ]
        
    def parse(self, response):
        
            tip = []
        
            tipExplain = []
        
            for tips in response.css("div.col-md-6 div.wysiwyg"):
        
                yield{
                    "tip" : tips.css("p::text").getall()
                }
                
                
            
              
       
           