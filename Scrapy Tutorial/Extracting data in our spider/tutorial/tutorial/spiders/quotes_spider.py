#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-23 23:19:50
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    运行：
    # 获得一个json格式的文件
    scrapy crawl quotes -o quotes.json

    # 获得一个json行的文件
    scrapy crawl quotes -o quotes.jl

    如果想要进行更复杂的操作，可以编写tutorial/pipelines.py文件
    
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            # 返回一个列表，列表包含下面的内容
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
