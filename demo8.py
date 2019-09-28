'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/11 16:33
@Software: PyCharm
@File    : demo8.py
'''
import time
from selenium import webdriver

driver_path = r'C:\geckodriver\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)

#通过driver打开两个网站，会在一个页面内进行切换
driver.get('https://www.baidu.com/')
# driver.get('https://www.douban.com/')

#在新的页面打开另一个网站，execute_script('window.open("url")'),但是python仍然指向第一个打开的网站
driver.execute_script('window.open("https://www.douban.com/")')
print(driver.current_url)#查看python当前指向的网站页面

print(driver.window_handles)#打印一下窗口句柄

#页面切换,需要等待一会，否则current_url会返回空about:blank
driver.switch_to.window(driver.window_handles[1])#switch_to.window切换窗口，window_handles选择要切换的窗口
time.sleep(1)

print(driver.current_url)#查看python当前指向的网站页面
print(driver.page_source)

#虽然在窗口中切换到了新的页面。但是driver中还没有切换。
#如果想要在代码中切换到新的页面，并且做一些爬虫。那么应该使用driver.switch_to.window来切换到指定的窗口，
#从driver.window_handlers中取出具体第几个窗口_
#driver.window_handlers是一个列表，里面装的都是窗口句柄。他会按照打开页面的顺序来存储窗口的句柄。
