'''
Created on 2019年3月21日

@author: NERO
'''
import configparser,os,requests,random,time,ssl

from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from selenium import webdriver
from lxml import etree

base = os.path.dirname(__file__)            #文件目录
base = os.path.dirname(base)                #上一级目录
base = os.path.dirname(base)                #上二级目录
conf_path = os.path.join(base,"conf.ini")
config  = configparser.ConfigParser()
config.read(conf_path)
url = 'https://ip.cn'#https://www.ipip.net/'     #config['DEFAULT']['url']
keyword = config['DEFAULT']['keyword']

user_agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
proxies=[{'http':'http://117.191.11.71:80','https':'https://115.159.206.127:80'},\
        {'http':'http://117.191.11.112:80','https':'https://118.89.138.129:59460'}, \
        {'http':'http://101.37.20.241:443','https': 'https://223.166.247.206:9000'},\
        {'http':'http://39.137.46.75:80','https':'https://60.190.153.150:8080'} ,\
        {'http':'socks5://36.32.24.170:1080','https':'socks5://36.32.24.170:1080'},\
        {'http':'socks5://106.14.225.196:8082','https':'socks5://106.14.225.196:8082'} ]
ssl._create_default_https_context = ssl._create_unverified_context
content = requests.get(url,headers = {'User-Agent': random.choice(user_agent)},\
                        proxies=proxies[0],verify=False).text

# doc = pq(content)
# pages = doc('.thumb-container a')
# print(len(pages))
# for page in pages:
#     navi = pq(page)
#     realurl = keyword + navi.attr.href
#     photo = pq(requests.get(realurl,headers={'Connection':'close'},proxies=random.choice(proxies)).text)
#     lis = photo('#image-container a')('img').attr('src')
#     print(lis)
#     time.sleep(1)

#检测当前访问使用的IP地址
html=etree.HTML(content)
try :
    ip=html.xpath('//div[@class="yourInfo"]/ul/li[1]/a/text()')
    print(ip)
except:
    ip=html.xpath('/html/body/div/center/text()')[0]
    print("当前请求IP地址为："+ip)

browser = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
browser.get(url)
print(browser.page_source)

