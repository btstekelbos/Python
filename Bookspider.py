import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "urlcrawler"
    allowed_domains = ["toscrape.com/"]
    start_urls = ["https://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow = "catalogue/category")),
        Rule(LinkExtractor(allow = "catalogue", deny = "category"), callback= "parse_item" )


    )
    def parse_item(self, response):
        
        yield{
            "title" : response.css("div.product_main h1::text").get(),
            "price" : response.css("p.price_color::text").get(),
            "availability" : response.css("p.availability::text")[1].get().replace(" ", "").replace("\n", "")
        }






