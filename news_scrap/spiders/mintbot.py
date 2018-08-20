# -*- coding: utf-8 -*-
import scrapy
from dateutil import parser

from  news_scrap.items import SmintItem

class MintbotSpider(scrapy.Spider):
    name = 'mintbot'
    start_urls = ['https://www.steelmint.com/ajax_calls.php?getMoreNews=true']

    def parse(self, response):
        for i in range(1, 2): #only first two pages
            url = "https://www.steelmint.com/ajax_calls.php?getMoreNews=true&page="+str(i)
            #url = start_urls[0] + "&page="+ str(i+1)
            yield scrapy.Request(url, self.parse_page)

    def parse_page(self, response):
        urls = response.css("a.news-url::attr(href)").extract()
        for url in urls:
            yield response.follow(url, self.parse_article)

    def parse_article(self, response):
        item = SmintItem()
        item["headline"] = response.xpath("//meta[@name='subject']/@content").extract()
        item["description"] = response.xpath("//meta[@name='description']/@content").extract()
        d = (response.css(".post-date::text").extract_first()).replace('Posted on ','')
        item["date"] = parser.parse(d.strip())
        item["category"] = (response.css(".label::text").extract())[0].strip()
        return item
