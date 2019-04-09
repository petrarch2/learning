#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/4/9'

import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_request(url):
    result = requests.get(url)
    print(result.text)

url = "https://www.taobao.com"
#线程池中最多能同时运行的线程数目(10)
executor = ThreadPoolExecutor(10)
task1 = executor.submit(fetch_request, url)
executor.shutdown(True)