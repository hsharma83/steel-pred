# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import scrapy

from news_scrap.items import MetaljunctionItem

class ArticleSpider(scrapy.Spider):
    name = "article"
    custom_settings = {'FEED_URI': 'metaljunction.csv'}
    start_urls = [
            "https://www.metaljunction.com/news/newslist/",
        ]

    def parse(self, response):
        people = response.css('ul#metal-news-list.news-list li')
        for person in people:
            item = MetaljunctionItem()
            item['title'] = person.css('a::text').extract_first()
            item['date'] = person.css('span.date::text').extract_first()
            #item['content'] = person.css('div.text div::text').extract_first()
            yield item

        #*This section is not required as we are daily scrapping*
        #next_page = response.css('ul#newPage a::attr(href)').extract()[-2]
        #if next_page is not None:
        #    yield response.follow(next_page, callback=self.parse)
