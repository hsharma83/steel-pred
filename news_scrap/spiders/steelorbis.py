# -*- coding: utf-8 -*-
import scrapy

from steelnews.items import SteelorbisItem

class SteelorbisSpider(scrapy.Spider):
    name = 'steelorbis'
    custom_settings = {'FEED_URI': 'steelorbis.csv'}
    start_urls = ['https://www.steelorbis.com/taxonomy/steel-news/?page=']

    def parse(self, response):
    	for i in range(1,20):
    		url = "https://www.steelorbis.com/taxonomy/steel-news/?page="+str(i)
    		yield scrapy.Request(url, self.parse_page)

    def parse_page(self, response):
        rows = response.xpath('//table[@id="article"]/tbody/tr')
        for row in rows:
            item = SteelorbisItem()
            item['title'] = row.xpath('td[3]/a//text()').extract()
            item['date'] = row.xpath('td[1]/span//text()').extract()
            yield item
