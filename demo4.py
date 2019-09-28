'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/9 19:26
@Software: PyCharm
@File    : demo4.py
'''
#常见的表单元素 input type='text/password/email/number' 文本框，
#button input='submit' 按钮
#checkbox input='checkbox'
#select 下拉列表

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver_path = r'C:\geckodriver\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
#操作输入框
driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')

time.sleep(5)

inputTag.clear()#清除输入框内容

#操作checkbox勾选框
driver.get('https://www.douban.com/')

inputTag1 = driver.find_element_by_name('remember')
inputTag1.click()#选中checkbox框，取消选中调用两次click

#操作select标签
driver.get('http://www.dobai.cn/')
select = Select(driver.find_element_by_name('jumpMenu'))
select.select_by_index(1)#根据索引值选择页面
select.select_by_value('http://m.95xiu.com/')#根据value值跳转页面
select.select_by_visible_text('95秀')#根据可见文本选择页面
select.deselect_all()#取消所有选中

#操作按钮的点击事件
driver.get('https://www.baidu.com/')
inputTag2 = driver.find_element_by_id('kw')
inputTag2.send_keys('python')#输入关键词

submitTag = driver.find_element_by_id('su')
submitTag.click()#点击按钮