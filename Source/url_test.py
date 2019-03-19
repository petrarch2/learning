#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/3/18'

import configparser,os
import urllib.request,urllib.parse,socket,urllib.error
import requests

# base = os.path.splitdrive(os.path.realpath(__file__))[0]
# base = os.path.realpath(__file__).split('\\')
# conf_path = os.path.join(base[0]+'\\',base[1],"conf.ini")
base = os.path.dirname(__file__)            #文件目录
base = os.path.dirname(base)                #上一级目录
base = os.path.dirname(base)                #上二级目录
conf_path = os.path.join(base,"conf.ini")
config  = configparser.ConfigParser()
config.read(conf_path)
url = config['DEFAULT']['url']
if 0:
    #post方式请求
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')    #将字典转换为url参数
    response = urllib.request.urlopen('http://httpbin.org/post', data=data)     #data要是字节流编码格式的内容，即 bytes 类型
    print(response.read().decode('utf-8'))

    #get方式请求
    try:
        print(urllib.request.urlopen('http://www.baidu.com',timeout = 0.1).read().decode('utf-8'))
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')
    except urllib.error.HTTPError as e:
        print(e.reason)
    else:
        print("reqeust successfully")

    #通过urllib.request.Request给请求添加头部信息
    headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'bilibili.com'
}
    request = urllib.request.Request('https://bilibili.com',headers=headers)
    # request.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)\
    #  AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    response = urllib.request.urlopen(request)
    for k, v in response.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', response.read().decode('utf-8'))

    #解析网址
    result = urllib.parse.urlparse("https://bilibili.com")
    print(result)

    #通过ProxyHandler设置代理
    proxy_handler = urllib.request.ProxyHandler({
        'http': 'http://111.177.169.246:9999',
        'https': 'https:/115.29.170.58:8118'
    })
    opener = urllib.request.build_opener(proxy_handler)
    response = opener.open('https://bilibili.com')

else:
    response = requests.get(url)
    print(response.encoding)
    print(response.content.decode("utf-8"))

