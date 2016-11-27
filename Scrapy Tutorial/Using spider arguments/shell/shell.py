#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-27 21:16:48
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    # 创建scrapy项目
    scrapy startproject myproject [project_dir]
    这个命令将会创建一个 project_dir 目录，并在里面创建一个 myproject 的
    scrapy项目，如果没有指定文件夹名称，将会使用项目名称创建一个文件夹。

    # 进入刚才创建的项目
    cd project_dir 

    # 创建一个新的爬虫
    scrapy genspider mydomain mydomain.com
    # 会创建一个 spiders/mydomain.py 文件，内容如下：
    """
        # -*- coding: utf-8 -*-
        import scrapy


        class MydomainSpider(scrapy.Spider):
            name = "mydomain"
            allowed_domains = ["mydomain.com"]
            start_urls = (
                'http://www.mydomain.com/',
            )

            def parse(self, response):
                pass

    """

    # 一般的命令都是在项目内部运行的，哪些命令在哪里运行参考下面的文档：
    https://doc.scrapy.org/en/1.2/topics/commands.html#topics-commands-ref

    # 获得命令帮助
    scrapy <command> -h

    # 查看所有的可用命令
    scrapy -h

    # 全局命令
    startproject
    genspider
    settings
    runspider
    shell
    fetch
    view
    version

    # 仅项目内部使用的命令
    crawl
    check
    list
    edit
    parse
    bench

    # ------------------------------------------------
    # startproject 用来创建一个项目
    # 是否需要一个项目：否
    scrapy startproject <project_name> [project_dir]
    
    # ------------------------------------------------
    # genspider 在当前文件夹或者当前项目的spiders文件夹，创建一个爬虫
    # 是否需要一个项目：否
    # 这个命令可以用来创建基于预定义模板的爬虫，当然也可以自己手动创建这些文件，
    # 因为这并不是唯一的方式
    # name 为爬虫的名称
    # domain 用来生成 allowed_domains 和 start_urls 参数
    # 用法示例
    """
        $ scrapy genspider -l
        Available templates:
          basic
          crawl
          csvfeed
          xmlfeed

        $ scrapy genspider example example.com
        Created spider 'example' using template 'basic'

        $ scrapy genspider -t crawl scrapyorg scrapy.org
        Created spider 'scrapyorg' using template 'crawl'
    """
    scrapy genspider [-t template] <name> <domain>
    
    # ------------------------------------------------
    # crawl 启动一个爬虫
    # 是否需要一个项目：是
    # spider 爬虫的name
    # 用法示例
    """
        $ scrapy crawl myspider
        [ ... myspider starts crawling ... ]
    """
    scrapy crawl <spider>

    # ------------------------------------------------
    # check 检查爬虫
    # 是否需要一个项目：是
    # 用法示例
    """
        $ scrapy check -l
        first_spider
          * parse
          * parse_item
        second_spider
          * parse
          * parse_item

        $ scrapy check
        [FAILED] first_spider:parse_item
        >>> 'RetailPricex' field is missing

        [FAILED] first_spider:parse
        >>> Returned 92 requests, expected 0..4
    """
    scrapy check [-l] <spider>
    
    # ------------------------------------------------
    # list 列出当前项目中所有可用的爬虫，每行一个
    # 是否需要一个项目：是
    # 用法示例
    """
        $ scrapy list
        spider1
        spider2
    """

    # ------------------------------------------------
    # edit 使用 EDITOR 中设置的编辑器来编辑指定的爬虫
    # 是否需要一个项目：是
    # 用法示例
    """
        scrapy edit spider1
    """
    scrapy edit <spider>

    # ------------------------------------------------
    # fetch 使用scrapy的下载器来下载一个页面，并将内容写入标准输出
    # 是否需要一个项目：否
    # 如果这个命令在爬虫项目的外部使用，则使用默认内置的下载行为
    # 如果在项目内部使用，则使用爬虫内部的配置。
    # 例如，如果爬虫具有覆盖用户代理的USER_AGENT属性，那么它将使用该代理。
    # 使用这个命令还能看到爬虫如何获取一个页面的
    # 用法示例
    """
        $ scrapy fetch --nolog http://www.example.com/some/page.html
        [ ... html content here ... ]

        $ scrapy fetch --nolog --headers http://www.example.com/
        {'Accept-Ranges': ['bytes'],
         'Age': ['1263   '],
         'Connection': ['close     '],
         'Content-Length': ['596'],
         'Content-Type': ['text/html; charset=UTF-8'],
         'Date': ['Wed, 18 Aug 2010 23:59:46 GMT'],
         'Etag': ['"573c1-254-48c9c87349680"'],
         'Last-Modified': ['Fri, 30 Jul 2010 15:30:18 GMT'],
         'Server': ['Apache/2.2.3 (CentOS)']}
    """
    scrapy fetch <url>

    # ------------------------------------------------
    # view 下载页面并在浏览器中打开下载的页面，可以以此来检查爬虫看到了什么
    # 是否需要一个项目：否
    # 用法示例
    """
        $ scrapy view http://www.example.com/some/page.html
        [ ... browser starts ... ]
    """
    scrapy view <url>

    # ------------------------------------------------
    # shell 启动给定url的shell环境，如果没有指定url则为空
    # 是否需要一个项目：否
    # 用法示例
    """
        $ scrapy shell http://www.example.com/some/page.html
        [ ... scrapy shell starts ... ]
    """
    scrapy shell [url]

    # ------------------------------------------------
    # parse 
    # 是否需要一个项目：是


"""
