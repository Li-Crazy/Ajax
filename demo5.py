'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/9 20:04
@Software: PyCharm
@File    : demo5.py
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'C:\geckodriver\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('https://www.baidu.com/')

#创建行为链
#1.选中相关元素
inputTag = driver.find_element_by_id('kw')
submitTag = driver.find_element_by_id('su')
#2.创建行为链
antions = ActionChains(driver)
#把鼠标移动到input标签上
antions.move_to_element(inputTag)
#向标签内输入内容
antions.send_keys(inputTag,'python')
#把鼠标移动到点击按钮上
antions.move_to_element(submitTag)
#点击按钮
antions.click(submitTag)
# antions.click_and_hold()#点击但不松开鼠标
# antions.context_click()#右键点击
# antions.double_click()#双击
#执行行为链
antions.perform()
