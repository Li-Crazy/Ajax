'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/11 17:44
@Software: PyCharm
@File    : demo9.py
'''
from selenium import webdriver
import time
from selenium.webdriver.common.proxy import *


## 第一步：创建一个FirefoxProfile实例
profile = webdriver.FirefoxProfile()
## 第二步：开启“手动设置代理”
profile.set_preference('network.proxy.type', 1)
## 第三步：设置代理IP
profile.set_preference('network.proxy.http', '27.154.34.146')
## 第四步：设置代理端口，注意端口是int类型，不是字符串
profile.set_preference('network.proxy.http_port', 30450)

profile.update_preferences()


driver_path =  r'C:\geckodriver\geckodriver.exe'
# #chrome设置代理
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=https://222.189.144.16:9999")

driver = webdriver.Firefox(executable_path=driver_path,firefox_profile=profile)

driver.get('http://www.httpbin.org/ip')