#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-22 21:41:26
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    运行：
        scrapy runspider quotes_spider.py -o quotes.json
        
        后面的参数，是使用feed导出的，可以轻松的更改格式。
        如：xml，csv，也可以通过编写项目管道存储在数据库中。
"""
import scrapy


# 爬虫的主体类，需要继承scrapy.Spider
class QuotesSpider(scrapy.Spider):
    # 爬虫的名称，这是唯一的
    name = "quotes"
    # 爬虫抓取的列表
    start_urls = [
        'http://quotes.toscrape.com/tag/humor'
    ]

    """
        解析方法
        Scrapy的请求是异步的，所以请求响应以后会回调这个方法，
        并把对应的response对象，传递过来。
    """
    def parse(self, response):
        # 使用css选择器，获取所有div下class为quote的元素
        for quote in response.css('div.quote'):
            # 每次返回一个
            yield {
                """
                    css选择器，选择span下的class为text的元素内的文本
                    extract_first 提取第一个内容
                """
                'text': quote.css('span.text::text').extract_first(),
                # xpath选择器，选择span下的small元素内的文本
                'author': quote.xpath('span/small/text()').extract_first(),
            }

            # 选择li元素下class为next里面的a标签的href属性
            next_page = response.css('li.next a::attr("href")').extract_first()
            # 如果获取到的地址不为空的话
            if next_page is not None:
                # 把xx.html这种地址变成http://www.baidu.com/xx.html
                next_page = response.urljoin(next_page)
                # 请求新的地址，并且把请求的结果响应给parse方法
                yield scrapy.Request(next_page, callback=self.parse)
