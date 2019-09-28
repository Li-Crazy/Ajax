'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/10 16:53
@Software: PyCharm
@File    : demo7.py
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver_path = r'C:\geckodriver\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('https://www.baidu.com/')

# driver.implicitly_wait(20)#隐式等待，获取不可用元素之前等待20秒，20秒后抛出异常

# driver.find_element_by_id('adffdd')

#显式等待，某个条件成立后才执行获取元素的操作，指定最大等待时间，超时则抛出异常
# WebDriverWait(driver,10).until(
#     EC.presence_of_element_located((By.ID,'asfsdsasd'))
# )
element = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.CLASS_NAME,'s_ipt'))
)
print(element)
