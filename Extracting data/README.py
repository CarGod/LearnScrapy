#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-23 22:12:30
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    输入以下命令，进入scrapy的shell：
    scrapy shell "http://quotes.toscrape.com/page/1/"

    # --------------------CSS选择器------------------------

    # 获得页面的title标签对象
    response.css('title')

    # 获得title标签里面文本内容的对象，并从对象中提取包含的文字
    response.css('title::text').extract()
    # ['Quotes to Scrape']

    # 获得title标签对象，并提取对象里面的内容
    response.css('title').extract()
    # ['<title>Quotes to Scrape</title>']

    # extract提取的是所有，返回一个列表，此时如果要提取第一个对象里面的内容
    response.css('title::text').extract_first()
    # 'Quotes to Scrape'

    # 或者使用列表选择第一个对象，然后使用extract提取里面的内容，也可以达到获取一个的效果
    response.css('title::text')[0].extract()
    # 'Quotes to Scrape'

    # extract_first方法如果当一个元素不存在时会返回None，并不会出现空指针异常

    # 也可以使用re来用正则表达式匹配内容

    # 获得title文本里面以Quotes开头后跟任意多个字符的字符串
    response.css('title::text').re(r'Quotes.*')
    # ['Quotes to Scrape']

    # 获得以Q开头，后面跟任意多个字母的字符串
    response.css('title::text').re(r'Q\w+')
    # ['Quotes']

    # 获得任意多个字母，一个空格，后面跟一个to，一个空格，任意多个字母的字符串
    # 但是返回的时候只返回括号括起来的内容，他们被存放在一个列表里面
    response.css('title::text').re(r'(\w+) to (\w+)')
    # ['Quotes', 'Scrape']

    # --------------------XPath选择器------------------------

    # 选择title标签的对象
    response.xpath('//title')
    # [<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]

    # 选择所有title标签对象里面的文本对象列表的第一个里面的内容
    response.xpath('//title/text()').extract_first()
    # 'Quotes to Scrape'

    # <div class="quote">
    #     <span class="text">“The world as we have created it is a process of our
    #     thinking. It cannot be changed without changing our thinking.”</span>
    #     <span>
    #         by <small class="author">Albert Einstein</small>
    #         <a href="/author/Albert-Einstein">(about)</a>
    #     </span>
    #     <div class="tags">
    #         Tags:
    #         <a class="tag" href="/tag/change/page/1/">change</a>
    #         <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
    #         <a class="tag" href="/tag/thinking/page/1/">thinking</a>
    #         <a class="tag" href="/tag/world/page/1/">world</a>
    #     </div>
    # </div>

    scrapy shell "http://quotes.toscrape.com"

    # 提取div下的class为quote的元素
    response.css("div.quote")

    # 返回的是一个列表，我们来选择第一个
    quote = response.css("div.quote")[0]

    # 从刚才获得的quote对象中，获得title，author和tags
    # 从quote里面选择span标签下的class为text的元素，获得他的文本对象
    # 并且提取这个对象里面存储的内容
    title = quote.css("span.text::text").extract_first()
    # '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'

    # 从quote对象中选择small元素里面class为author的元素的文本对象，提取里面的内容
    author = quote.css("small.author::text").extract_first()
    # 'Albert Einstein'
    
    # 获取标签列表
    # 获得div标签下的class为tags的元素，获得他们里面的a标签下class为tag的元素里面的文本对象
    # 并且提取这些所有对象里面的文本，以列表的形式赋值给tags变量
    tags = quote.css("div.tags a.tag::text").extract()
    # ['change', 'deep-thoughts', 'thinking', 'world']
    
    # 把text, author, tags 放在一个字典里
    for quote in response.css("div.quote"):
        text = quote.css("span.text::text").extract_first()
        author = quote.css("small.author::text").extract_first()
        tags = quote.css("div.tags a.tag::text").extract()
        print(dict(text=text, author=author, tags=tags))

"""
