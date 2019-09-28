'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/4 20:14
@Software: PyCharm
@File    : demo1.py
'''
from selenium import webdriver

driver_path = r'C:\geckodriver\geckodriver.exe'

driver = webdriver.Firefox(executable_path=driver_path)

driver.get('https://www.baidu.com/')

print(driver.page_source)#获取网页源代码