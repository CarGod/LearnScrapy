#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-22 22:36:31
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    在命令行输入以下命令，新建一个scrapy项目：
        scrapy startproject tutorial

        创建完成以后，目录结构应该如下：
            tutorial/
                scrapy.cfg            # 配置文件

                tutorial/             # 实际的代码存放在这个文件夹
                    __init__.py

                    items.py          # items定义文件

                    pipelines.py      # pipelines文件

                    settings.py       # 设置文件

                    spiders/          # 一个文件夹，爬虫存放在这里
                        __init__.py

    在tutorial/spiders新建文件quotes_spider.py
    在命令行输入以下内容运行爬虫：
    scrapy crawl quotes
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    # 同一个项目中，必须是唯一的
    name = "quotes"

    """
        必须返回一个可迭代的Requests，可以是一个列表，
        也可以是一个生成器函数。也可以使用start_urls名称的
        列表来代替。
        后面的请求，也将通过这个方法来获取。
    """
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    """
        解析方法
    """
    def parse(self, response):
        """
            http://quotes.toscrape.com/page/1/ 根据 / 截取
            倒数第一个元素，也就是下标为-1的位置是空字符
            -2个元素就是数字1，也就是页码。
        """
        page = response.url.split("/")[-2]
        filename = 'quotes-{0}.html'.format(page)
        with open(filename, 'wb') as f:
            # 写出相应内容的body
            f.write(response.body)
        # 在控制台输出日志内容
        self.log('Saved file {0}'.format(filename))
