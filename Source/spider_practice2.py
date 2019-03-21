'''
Created on 2019年3月21日

@author: NERO
'''
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

doc = pq(content)
#print(doc)
pages = doc('.thumb-container a')
for page in pages:
    navi = pq(page)
    realurl = keyword + navi.attr.href
    photo = pq(realurl)
    lis = photo('#image-container a')('img').attr('src')
    print(lis)


