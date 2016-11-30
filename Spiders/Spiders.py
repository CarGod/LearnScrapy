#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-30 22:49:56
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    每个爬虫都要继承scrapy.Spider，
    它不提供任何特殊的功能，只是为每个爬虫默认实现了一个
    start_requests方法，以及start_urls属性发送请求，并为
    每个结果调用spider的方法解析。

    # name
    # 是否必须：是
    # 是否唯一：是
    爬虫的名称，必须是唯一的，因为它决定了scrapy如何定位和
    实例化一个爬虫。如果爬虫只是抓取单个域名，通常的做法是
    以域名来命名，比如抓取baidu.com的爬虫，就以baidu作为name
    
    # allowed_domains
    # 是否必须：否
    一个可选的字符串列表，说明那些域名是爬虫可以抓取的。

    # start_urls
    一个字符串列表，说明爬虫默认一开始访问哪些网站。

    # custom_settings
    对爬虫的配置，它将覆盖项目的默认配置，它必须被定义为类的属性。
    可用内置参数设置：
    https://doc.scrapy.org/en/1.2/topics/settings.html#topics-settings-ref

    # crawler
    这个属性是由初始化类后的from_crawler()方法设置，并绑定到此爬虫的Crawler对象。
    Crawlers在项目中封装了很多组件，用于单个条目访问（例如扩展，中间件，信号管理器等）。
    抓取工具API：
    https://doc.scrapy.org/en/1.2/topics/api.html#topics-api-crawler

"""
