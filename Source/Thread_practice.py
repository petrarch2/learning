#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/4/9'

import urllib.request,urllib.parse,urllib.error
from urllib import robotparser
import csv,time,re
from urllib.error import URLError
import lxml.html
import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_request(url):
    result = requests.get(url)
    print(result.text)

# url = "https://www.taobao.com"
# #线程池中最多能同时运行的线程数目(10)
# executor = ThreadPoolExecutor(10)
# task1 = executor.submit(fetch_request, url)
# executor.shutdown(True)

def dowmlpad(url, user_agent='wswp', proxy=None, num_retries=2, timeout=5):
    """
    #支持500重试
    #支持用户代理
    #支持IP代理
    """
    print('DownloadURL:', url)

    # 配置用户代理
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    # 配置
    opener = urllib.request.build_opener()

    # 判断是否代理
    if proxy:
        proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))

    try:
        html = opener.open(request, timeout=timeout).read()
    except urllib.request.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                html = dowmlpad(url, user_agent, num_retries - 1)
    except Exception as e:
        print('error:', e)
        html = None

    return html

class Timedelay:
    #初始化
    def __init__(self,delay):
        #设置延迟时间
        self.delay=delay
        #创建记录主站的字典
        self.domains={}
    #创建等待函数，同时还要实现记录走后一次访问时间
    def wait(self,url):
        netloc=urllib.parse.urlparse(url).netloc
        last_time=self.domains.get(netloc)
        if self.delay and last_time:
            sleeptime=self.delay-(time.time()-last_time)
            if sleeptime>0:
                time.sleep(sleeptime)
        #每次暂停后，或者没暂停都重置最后一次访问时间
        self.domains[netloc]=time.time()


def get_link(html):
    webpage_patt = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_patt.findall(html.decode())  # 返回一个包含所以页面link的列表


# 编写爬取规则，获取数据
def scrape_callback(url, html):
    csslist = ['span[property = "v:itemreviewed"]', 'span.year', 'strong[property = "v:average"]']
    try:
        tree = lxml.html.fromstring(html)
        row = [tree.cssselect('{0}'.format(field))[0].text for field in csslist]
        print(url, row)
    except Exception as e:
        print("ScrapeCallback error:", e)


def link_crawler(seed_url, link_regex, max_depath=2, scrape_callback=None):
    crawl_queue = [seed_url]  # 配置爬取队列，存储URL
    seens = {seed_url: 1}

    # 读取robots.txt
    #     rp=robotparser.RobotFileParser()
    #     rp.set_url('http://example.webscraping.com/robots.txt')
    #     rp.read()
    #     timedelay=Timedelay(None)     #同样是初始化

    # 循环到队列为空退出
    while crawl_queue:
        url = crawl_queue.pop()  # 移除队列最后一个元素并返回
        # 检查该url是否能被禁止爬取
        #         if rp.can_fetch(User_agent,url):
        #             timedelay.wait(url)       #暂停，并记下本次主站下载开始时间
        html = dowmlpad(url)  # 下载页面
        depth = seens[url]  # 获取现在的深度
        print(depth)

        # 获取页面中的连接
        for link in get_link(html):
            if depth != max_depath and re.search(link_regex, link):
                link = urllib.parse.urljoin(seed_url, link)  # 拼接连接

                if link not in seens:  # 先筛选符合条件的link，再进行筛选是否看过，这个顺序能减少工作量。
                    seens[link] = depth + 1
                    crawl_queue.append(link)

        if scrape_callback:
            scrape_callback(url, html)


class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open(r'D:\BDdownloads\example.csv', 'w', newline=''))
        self.fields = ['name', 'year', 'score']
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        csslist = ['span[property = "v:itemreviewed"]', 'span.year', 'strong[property = "v:average"]']
        try:
            tree = lxml.html.fromstring(html)
            row = [tree.cssselect('{0}'.format(field))[0].text for field in self.fields]
            self.writer.writerow(row)
        except Exception as e:
            print("ScrapeCallback error:", e)


def download(url, User_agent='wswp', proxy=None, num_retry=2):
    print('Downloading:', url)
    headers = {'User-agent': User_agent}
    request = urllib.request.Request(url, headers=headers)
    # 加入代理服务器的处理，就不用urlopen来下载网页了，而是用自己构建的opener来打开

    opener = urllib.request.build_opener()
    # 若设置了代理，执行下面操作加入代理到opener中
    if proxy:
        proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))  # 在自己构建的浏览器中加入了代理服务器
    # 当没有设置代理时，下面的打开方式和urlopen是一样的
    try:
        html = opener.open(request).read()
    except URLError as e:  # 引入URLError进行分析
        html = None
        print('Download error:', e.reason)
        if num_retry > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retry=num_retry - 1)

    return html

if __name__ == "__main__":
    send_url = 'https://movie.douban.com'
    link_regex = '/subject/[\d]+/'
    # link_crawler(send_url, link_regex, max_depath=2, scrape_callback=ScrapeCallback())
    # link_crawler(send_url,link_regex,max_depath=2,scrape_callback=scrape_callback)
    html=download(send_url).decode()     #lxml的输入要是字符串形式
    tree=lxml.html.fromstring(html)
    td=tree.cssselect('tr#places_area__row>td.w2p_fw')[0]       #cssselect选择出来的是一个列表，所以要取出里面的元素
    ares=td.text_content()
    print(ares)