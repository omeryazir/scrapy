# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyExampleItem

class StackoverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    allowed_domains = ['https://stackoverflow.com']
    start_urls = ['https://stackoverflow.com']

    def parse(self, response):
        question = response.css('.question-summary')
        for q in question:
            title = q.css('.question-hyperlink::text').extract_first()
            item = ScrapyExampleItem()
            item ['title'] = title
            yield item
