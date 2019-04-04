'''
Created on 2019年3月21日

@author: NERO
'''
import configparser,os,requests,random,time,ssl,re,json
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree

base = os.path.dirname(__file__)            #文件目录
base = os.path.dirname(base)                #上一级目录
base = os.path.dirname(base)                #上二级目录
conf_path = os.path.join(base,"conf.ini")
config  = configparser.ConfigParser()
config.read(conf_path)
url = config['DEFAULT']['url']
keyword = config['DEFAULT']['keyword']

def parse_html(html):
    '''
    :param html: 传入html源码
    :return: 通过yield生成一个生成器，存储爬取的每行信息
    '''
    soup = BeautifulSoup(html, 'lxml')

    table = soup.find("table", attrs={"id": "report"})
    trs = table.find("tr").find_next_siblings()
    for tr in trs:
        tds = tr.find_all("td")
        yield [
            tds[0].text.strip(),
            tds[1].text.strip(),
            tds[2].text.strip(),
            tds[3].text.strip(),
            tds[4].text.strip(),
            tds[5].text.strip(),
            tds[6].text.strip(),
            tds[7].text.strip(),
            tds[8].text.strip(),
        ]

def write_to_file(content):
    '''
    :param content:要写入文件的内容
    '''
    with open("result.txt",'a',encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")

if 0:
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
    proxies=[{'http':'http://39.106.35.21:3128','https':'https://39.106.35.21:3128'},\
            {'http':'socks5://123.58.55.162:1080','https':'socks5://123.58.55.162:1080'}, \
            {'http':'socks5://122.226.135.89:1080','https':'socks5://122.226.135.89:1080'},\
            {'http':'socks5://112.16.5.62:1080','https':'socks5://112.16.5.62:1080'} ,\
            {'http':'socks5://124.65.117.38:7302','https':'socks5://124.65.117.38:7302'},\
            {'http':'socks5://106.14.225.196:8082','https':'socks5://106.14.225.196:8082'} ]
    ssl._create_default_https_context = ssl._create_unverified_context
    content = requests.get(url,headers = {'User-Agent': random.choice(user_agent)},\
                            proxies=proxies[4],verify=False).text


    doc = pq(content)
    pages = doc('.thumb-container a')
    print(len(pages))
    for page in pages:
        navi = pq(page)
        realurl = keyword + navi.attr.href
        photo = pq(requests.get(realurl,headers={'Connection':'close'},proxies=random.choice(proxies)).text)
        lis = photo('#image-container a')('img').attr('src')
        print(lis)
        #time.sleep(1)


    #检测当前访问使用的IP地址，测试代理IP是否可用
    html=etree.HTML(content)
    ip=html.xpath('//div[@class="yourInfo"]/ul/li[1]/a/text()')[0]
    print("当前请求IP地址为："+ip)


    #练习selenium+phantomjs
    browser = webdriver.Edge()#PhantomJS(executable_path='/usr/local/bin/phantomjs')
    browser.get('https://www.taobao.com')
    # print(browser.page_source)
    input_first = browser.find_element(By.ID,"q")
    input_second = browser.find_element_by_css_selector("#mtb")
    lis = browser.find_elements_by_xpath('//*[@id="q"]')
    print(input_first.get_attribute('class'))
    print(input_second.text)
    print(lis)
    input_first.send_keys("ipad")
    time.sleep(1)
    input_first.clear()
    input_first.send_keys("MakBook pro")
    button = browser.find_element_by_class_name('btn-search')
    button.click()

    browser.get("http://www.zhihu.com/explore")
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)
    print(browser.get_cookies())
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # browser.execute_script('alert("To Bottom")')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://www.baidu.com')
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(1)
    browser.get("http://www.taobao.com")
    browser.back()
    # browser.close()
    browser.quit()
else:
    url = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search_content.jsp'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    data = {
        'yzm':'PA5J',
        'ktrqks':'2019-04-17',
        'ktrqjs':'2019-04-17',
        'pagesnum':1
    }
    content = requests.post(url, headers=headers,data=data).text
    doc = pq(content)
    table = doc('.meneame a ')
    pages = int(re.sub("\D", "", str(table[len(table)-1].attrib)))
    data['pagesnum'] = pages
    print(pages)
    time.sleep(2)
    for i in range(1, pages+1):
        while True:
            data['pagesnum'] = i
            content = requests.post(url, headers=headers,data=data).text
            soup = BeautifulSoup(content, 'lxml')
            if type(soup.title) != type(None):
                print("系统繁忙，登录太频繁，ip被封锁")
                time.sleep(20)
                continue
            else:
                break
        res = parse_html(content)
        for j in res:
            write_to_file(j)
        print("爬取完第【%s】页,总共【%s】页" %(i,pages))
        time.sleep(random.uniform(1.1,5.0))
    else:
        print("爬取完毕")

