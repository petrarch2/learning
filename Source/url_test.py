#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/3/18'

import configparser,os
import urllib.request,urllib.parse,socket,urllib.error
import requests,json,re
#python $FileName$ build_ext --inplace
'''
正则表达式常用的匹配模式
\w      匹配字母数字及下划线
\W      匹配f非字母数字下划线
\s      匹配任意空白字符，等价于[\t\n\r\f]
\S      匹配任意非空字符
\d      匹配任意数字
\D      匹配任意非数字
\A      匹配字符串开始
\Z      匹配字符串结束，如果存在换行，只匹配换行前的结束字符串
\z      匹配字符串结束
\G      匹配最后匹配完成的位置
\n      匹配一个换行符
\t      匹配一个制表符
^       匹配字符串的开头
$       匹配字符串的末尾
.       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[....]  用来表示一组字符，单独列出：[amk]匹配a,m或k
[^...]  不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
*       匹配0个或多个的表达式
+       匹配1个或者多个的表达式
?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
{n}     精确匹配n前面的表示
{m,m}   匹配n到m次由前面的正则表达式定义片段，贪婪模式
a|b     匹配a或者b
()      匹配括号内的表达式，也表示一个组
'''
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
keyword = config['DEFAULT']['keyword']
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
    headers = {'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)\
        AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'}
    response = requests.get(url, headers=headers)
    print(response.encoding)
    print(response.status_code)
    # print(response.content.decode("utf-8"))
    content = response.text
    pattern = re.compile(keyword, re.S)     #将正则表达式编译成正则表达式对象，方便复用该正则表达式
    results = re.findall(pattern, content)#result = re.match('^.\w.\d{6}.\d{3}.$', content)
    print(len(results))

    for result in results:
        url, name, author, date = result
        print(url, name, author, date)

