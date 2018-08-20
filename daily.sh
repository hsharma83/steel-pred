#!/bin/sh
#This is a daily script for scraping news and formatting them in specific format

#go home
cd ~
#crawling for news
scrapy crawl mintbot
scrapy crawl steelorbis
scrapy crawl article
#formatting and prediction
python editcsv.py
python predict.py
python update_data.py
