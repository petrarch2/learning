#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/3/21'

import configparser,os,requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from selenium import webdriver


base = os.path.dirname(__file__)            #文件目录
base = os.path.dirname(base)                #上一级目录
base = os.path.dirname(base)                #上二级目录
conf_path = os.path.join(base,"conf.ini")
config  = configparser.ConfigParser()
config.read(conf_path)
url = config['DEFAULT']['url']
keyword = config['DEFAULT']['keyword']

content = requests.get(url).text
if 1:
    doc = pq(content)
    # print(doc)
    # print(type(doc))
    menu = doc('.desktop a')
    for char in menu:
        label = pq(char)
        print(label.text() ,':',label.attr.href)

    pages = doc('.pagination a')
    for page in pages:
        navi = pq(page)
        #<a href="?page=5" class="page">5</a>
        #print(navi.doc('.class_name') ,navi.text(), ':', navi.attr.href)

    items  = doc('.gallery')
    for item in items:
        lis = pq(item)('a')
        print(lis('.caption').text())
        print(lis('img').attr('data-src'))
        print(lis.attr.href)
        print(lis.parent().attr('data-tags'))
    print(len(items))



else:
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



    browser = webdriver.PhantomJS()
    browser.get(url)
    print(browser.page_source)