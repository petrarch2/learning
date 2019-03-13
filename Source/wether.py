#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import socket
import httplib2,urllib


params = urllib.parse.urlencode({'ip':'9.8.8.8','datatype':'jsonp','callback':'find'})
url = 'http://api.ip138.com/query/?'+params
headers = {"token":"8594766483a2d65d76804906dd1a1c6a"}#token为示例
http = httplib2.Http()
response, content = http.request(url,'GET',headers=headers)
print(content)

ip = socket.gethostbyname(socket.gethostname())#得到本地ip
ip_list = socket.gethostbyname_ex(socket.gethostname())#得到本地ip
apiurl = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' %ip
content = urllib.request.urlopen(apiurl).read()

province = urllib.request.urlopen('http://www.weather.com.cn/data/citydata/china.html').read().decode('utf-8')
city = urllib.request.urlopen('http://www.weather.com.cn/data/citydata/district/10121.html').read().decode('utf-8')
county = urllib.request.urlopen('http://www.weather.com.cn/data/citydata/city/1012101.html').read().decode('utf-8')
weather = urllib.request.urlopen('http://www.weather.com.cn/data/cityinfo/101210101.html').read().decode('utf-8')

print(ip_list)

try:
	c = open('test1.html','r',encoding='utf-8')
	d = c.read()
	c.close()
	#print(d)
except:
	print('file not exist')
	

print('\u676d\u5dde\u5e02')

