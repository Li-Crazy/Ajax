'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/12 9:04
@Software: PyCharm
@File    : demo10.py
'''
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver_path = r'C:\geckodriver\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get("https://www.baidu.com/")

submitBtn = driver.find_element_by_id('su')
print(type(submitBtn))#<class 'selenium.webdriver.firefox.webelement.FirefoxWebElement'>
print(submitBtn.get_attribute("value"))#获取标签中的value属性值
driver.save_screenshot("baidu.png")#页面截图