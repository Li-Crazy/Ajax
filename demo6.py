'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/9 20:46
@Software: PyCharm
@File    : demo6.py
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'C:\geckodriver\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('https://www.baidu.com/')

for cookie in driver.get_cookies():#获取所有的cookie信息
    print(cookie)

print(driver.get_cookie("PSTM"))#根据cookie中的某个key对应的value值获取cookie信息
driver.delete_cookie("PSTM")#根据key对应的value值删除cookie
driver.delete_all_cookies()#删除所有的cookie