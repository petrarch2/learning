#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/3/21'

import configparser,os,requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

#从配置文件读取网址
base = os.path.dirname(__file__)            #文件目录
base = os.path.dirname(base)                #上一级目录
base = os.path.dirname(base)                #上二级目录
conf_path = os.path.join(base,"conf.ini")
config  = configparser.ConfigParser()
config.read(conf_path)
url = config['DEFAULT']['url']
keyword = config['DEFAULT']['keyword']

#用requests获取网页信息
content = requests.get(url).text
#解析网页
if 1:
    # 练习pyquery
    doc = pq(content)
    # print(doc)
    # print(type(doc))
    menu = doc('.desktop a')
    for char in menu:
        label = pq(char)
        print(label.text() ,':',url+label.attr.href)

    pages = doc('.pagination a')
    for page in pages:
        navi = pq(page)
        #<a href="?page=5" class="page">5</a>
        print(navi.attr('class') ,navi.text(), ':', url+navi.attr.href)

    items  = doc('.gallery')
    for item in items:
        lis = pq(item)('a')
        print(lis('.caption').text())
        print(lis('img').attr('data-src'))
        print(url+lis.attr.href)
        print(lis.parent().attr('data-tags'))
    print(len(items))



else:
    # 练习BeautifulSoup
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
    print(soup.title)               #通过soup.标签名获得这个标签的内容
    print(soup.title.name)          #获得title标签的名称
    print(soup.title.string)        #获取第一个title标签的内容
    print(soup.title.parent.name)   #title标签父节点的名称
    print(soup.a["class"])
    print(soup.a)
    print(soup.find_all('a'))
    for link in soup.find_all('a'):
        print(link.get('href'))

    # print(soup.get_text())        #获取文本内容



