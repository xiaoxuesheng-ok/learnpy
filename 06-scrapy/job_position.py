# -*- coding: utf-8 -*-
import scrapy


class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['zhipin.com']
    start_urls = ['http://zhipin.com/']

    def parse(self, response):
        pass
