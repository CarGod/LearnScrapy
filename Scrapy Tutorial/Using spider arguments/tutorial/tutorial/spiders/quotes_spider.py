#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-27 20:19:08
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    携带命令行参数
    运行：
        scrapy crawl quotes -o quotes-humor.json -a tag=humor
    使用getattr(self, 参数名, 默认值)来进行获取
    getattr(self, 'tag', None) 将获取 humor，如果获取不到就返
    回默认值设置的内容，这里是None。
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        # 获取命令行传递的tag参数
        tag = getattr(self, 'tag', None)
        if tag is not None:
            # 这样拼接后url变成：http://quotes.toscrape.com/tag/humor
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small a::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)
