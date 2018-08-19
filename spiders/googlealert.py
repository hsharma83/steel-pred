# -*- coding: utf-8 -*-
import scrapy


class GooglealertSpider(scrapy.Spider):
    name = 'googlealert'
    custom_settings = {'FEED_URI': 'googlealert.csv'}
    allowed_domains = ['https://www.google.co.in/alerts/feeds/13465962862743070888/9464954343600699798']
    start_urls = ['https://www.google.co.in/alerts/feeds/13465962862743070888/9464954343600699798/']

    def parse(self, response):
        pass
