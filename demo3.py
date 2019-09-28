'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/4 20:14
@Software: PyCharm
@File    : demo1.py
'''
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By

driver_path = r'C:\geckodriver\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('https://www.baidu.com/')
print(driver.page_source)

html = driver.page_source
html.xpath("")
#1.如果只是想要解析网页中的数据。那么推荐将网页源代码扔給1xm1来解析。因为1xm1底层使用的是c语言，所以解析效率会更高。
#2.如果是想要对元素进行一些操作，比如给一个文本框输入值，或者是点击某个按钮，那么就必须使用selenium给我们提供的查找元素的方法。

#以百度首页输入框为例
#find_element 查找第一个元素， find_elements 查找多个元素
# inputTag = driver.find_element_by_id('kw')#根据id查找
# inputTag = driver.find_element(By.ID,'kw')#根据id查找
# inputTag.send_keys('python')#向inputTag里发送字符串

# inputTag1 = driver.find_element_by_name('wd')#通过name获取
inputTag1 = driver.find_element(By.NAME,'wd')#通过name获取
# inputTag1.send_keys('python')#向inputTag里发送字符串
#
# inputTag2 = driver.find_element_by_class_name('s_ipt')#通过class_name获取
inputTag2 = driver.find_element(By.CLASS_NAME,'s_ipt')#通过class_name获取
# inputTag2.send_keys('python')#向inputTag里发送字符串

# inputTag3 = driver.find_element_by_xpath('//input[@id="kw"]')#通过class_name获取
inputTag3 = driver.find_element(By.XPATH,'//input[@id="kw"]')#通过class_name获取
# inputTag3.send_keys('python')#向inputTag里发送字符串

# inputTag4 = driver.find_element_by_css_selector('.quickdelete-wrap > '
#                                                 'input')#通过css获取,需要加. ,>获取直接子元素
inputTag4 = driver.find_element(By.CSS_SELECTOR,'.quickdelete-wrap > input')
# inputTag4.send_keys('python')#向inputTag里发送字符串

# inputTag5 = driver.find_elements_by_css_selector('.quickdelete-wrap > input')[0]
inputTag5 = driver.find_elements(By.CSS_SELECTOR,'.quickdelete-wrap > input')[0]
#find_elements通过css获取多个元素,需要加. , >获取直接子元素
inputTag5.send_keys('python')#向inputTag里发送字符串


