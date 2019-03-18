#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/3/18'

import urllib.request,urllib.parse,socket

if 0:
    #post方式请求
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
    response = urllib.request.urlopen('http://httpbin.org/post', data=data)     #data要是字节流编码格式的内容，即 bytes 类型
    print(response.read().decode('utf-8'))

    #get方式请求
    try:
        print(urllib.request.urlopen('http://www.baidu.com',timeout = 0.1).read().decode('utf-8'))
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')

else:
    #通过urllib.request.Request给请求添加头部信息
    request = urllib.request.Request('https://bilibili.com')
    request.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)\
     AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    response = urllib.request.urlopen(request)
    for k, v in response.getheaders():
        print('%s: %s' % (k, v))
#     print('Data:', response.read().decode('utf-8'))
