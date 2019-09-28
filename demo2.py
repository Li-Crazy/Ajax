'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/4 20:14
@Software: PyCharm
@File    : demo1.py
'''
from selenium import webdriver
import time

driver_path = r'C:\geckodriver\geckodriver.exe'

driver = webdriver.Firefox(executable_path=driver_path)

driver.get('https://www.baidu.com/')

# print(driver.page_source)
time.sleep(5)
#
# driver.close()#关闭当前页面

driver.quit()#退出浏览器