#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-27 15:45:21
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    # 如果需要获取下一页的时候，页面中下一页的链接HTML代码如下
    <ul class="pager">
        <li class="next">
            <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
        </li>
    </ul>

    # 可以尝试在命令行中输入以下内容
    # 提取li标签下面class为next的下面的a标签，返回符合条件的第一个
    response.css('li.next a').extract_first()
    # <a href="/page/2/">Next <span aria-hidden="true">→</span></a>'

    # 如果想提取a标签的href里面的内容
    # 提取li标签下面的class为next的元素下面的a标签的href元素的对象，并且提取这个对象里面的内容
    response.css('li.next a::attr(href)').extract_first()
    # /page/2/
"""
