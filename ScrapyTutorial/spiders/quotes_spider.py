import scrapy
from ..items import ScrapytutorialItem

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    # link to scrape all the pages in the website
    #start_urls = [
    #    "https://quotes.toscrape.com/"
    #]
    
    # link to scrape pages but can limit them 
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]
    
    
    def parse(self, response):
        # Extracting by sentences
        #title = response.css("title::text").extract()
        #yield {'titletext' : title}
        
        #import items from items.py
        items = ScrapytutorialItem()
        
        # Extracting by blocks
        all_div_quotes = response.css("div.quote")
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            #Printing the result to terminal
            #yield{
            #    'title': title,
            #    'author': author,
            #    'tag': tag
            #}
            
            yield items
        
        #scrape all pages in 1 website
        #next_page = response.css('li.next a::attr(href)').get()
        
        #scrape pages but limit the number of pages 
        next_page = 'https://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number) + '/'
        
        #scrape all pages in the website
        #if next_page is not None:
        #    yield response.follow(next_page, callback = self.parse)
        
        if QuoteSpider.page_number < 11: #number of pages is smaller than 11
            QuoteSpider.page_number +=1
            yield response.follow(next_page, callback = self.parse)    
        
        