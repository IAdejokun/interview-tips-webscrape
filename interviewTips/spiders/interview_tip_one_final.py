import scrapy


class interviewTipsSpider(scrapy.Spider):
    name = "interview-one-final"
    
    start_urls=[
            "https://www.dol.gov/general/jobs/interview-tips/"
        ]
        
    def parse(self, response):
       
            todoArrQuestion = []
                
            todoArrAnswer = [] 
                
            for todo in response.css("h4.usa-accordion__heading"):
                todo_text = todo.css('button.usa-accordion__button::text').get()
                todoArrQuestion.append(todo_text)
            
            for todoAns in response.css("div.usa-accordion__content.usa-prose ul"):
                todo_text_ans = todoAns.css('li::text').getall()
                todoArrAnswer.append(todo_text_ans)  
            
            for key, value in zip(todoArrQuestion, todoArrAnswer):
                item = {'todo':key, 'todo-answer':value}
                
                yield item