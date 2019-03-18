#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/3/18'

config_str = '''
# 配置文件信息案例
[DEFAULT]
minSdkVersion = 15
targetSdkVersion = 24
versionName = 1.0.0
server action = yes
 
[NAME]
user = yamaP

[AGE]
age = 18

# This is a comments.
[mysql]
ip = 127.0.0.1
port = 3306
'''


import configparser,os
base = os.path.split(os.path.realpath(__file__))[0]   #获取本文件路径
conf_path = os.path.join(base,"config.ini")                #获取ini路径

config  = configparser.ConfigParser()
config['DEFAULT'] = {'minSdkVersion': '15',
                         'targetSdkVersion': '24',
                         'versionName': '1.0.0',
                         'server action': 'yes'}

config['NAME'] = {}
config['NAME']['user'] = 'yamaP'

config['AGE'] = {'age': '18'}

config['mysql'] = {}
topsecret = config['mysql']
topsecret['ip'] = '127.0.0.1'
topsecret['port'] = '3306'
with open('config.ini', 'w') as configfile:
    config.write(configfile)

config .read(conf_path)
lists_header = config.sections()  # 配置组名, ['NAME', 'AGE','mysql'] # 不含'DEFAULT'
print(lists_header)

boolean = 'NAME' in config  # 配置组是否存在
boolean = config.has_section("NAME")
print(boolean)

user = config['NAME']['user']
print(user)

mysql = config['mysql']
mysql_ip = mysql['ip']
mysql_port = mysql['port']
print(mysql_ip, ":", mysql_port)

# 删除
sec = config.remove_section("AGE")  # 删除
config.write(open("config.ini", "w"))

# 添加
config.add_section("web.server")
config.write(open("config.ini", "w"))

# 修改/添加
config.set("web.server", "http", "http://xxx")
test = config .getint("mysql","port")
test += 1
config.set("mysql", "port", str(test))
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# 删除key
config.remove_option("mysql", "ip")
config.write(open("config.ini", "w"))
