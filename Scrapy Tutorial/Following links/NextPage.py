#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-27 16:00:54
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        # 获取下一页a标签的链接地址
        next_page = response.css('li.next a::attr(href)').extract_first()

        # 判断是不是为空
        if next_page is not None:
            # 把/page/2/这种类型的url变成http://quotes.toscrape.com/page/2/
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=parse)
