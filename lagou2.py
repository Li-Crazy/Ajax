'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/12 10:31
@Software: PyCharm
@File    : lagou2.py
'''
from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LagouSpider(object):
    driver_path = r'C:\geckodriver\geckodriver.exe'
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=LagouSpider.driver_path)
        self.url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
        self.positions = []

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            # print(source)
            WebDriverWait(driver=self.driver,timeout=10).until(
                EC.presence_of_element_located((By.XPATH,"//div[@class='pager_container']/span[last()]"))
            )
            self.parse_list_page(source)
            try:
                next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
                if "pager_next pager_next_disabled" in next_btn.get_attribute("class"):
                    break
                else:
                    next_btn.click()
            except:
                print(source)
            time.sleep(1)

    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            # print(link)
            self.request_detail_page(link)
            time.sleep(1)
            # break

    def request_detail_page(self,url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # self.driver.get(url)
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='job-name']//span[@class='name']"))
        )
        source = self.driver.page_source
        # print(source)
        self.parse_detail_page(source)
        self.driver.close()#关闭当前页面
        self.driver.switch_to.window(self.driver.window_handles[0])#切换回主页面

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        # print(position_name)
        company_name = html.xpath("//h2[@class='fl']//text()")[1].strip()
        print(company_name)
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_spans[0].xpath('.//text()')[0].strip()
        # print(salary)
        city = job_request_spans[1].xpath('.//text()')[0].strip()
        city = re.sub(r'[\s/]', '', city)
        # print(city)
        work_years = job_request_spans[2].xpath('.//text()')[0].strip()
        work_years = re.sub(r'[\s/]', '', work_years)
        # print(work_years)
        education = job_request_spans[3].xpath('.//text()')[0].strip()
        education = re.sub(r'[\s/]', '', education)
        # print(education)
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()  # join()将列表转换为字符串
        # print(desc)
        position = {
            'name':position_name,
            'company_name':company_name,
            'salary':salary,
            'city':city,
            'work_years':work_years,
            'education':education,
            'desc':desc
        }
        self.positions.append(position)
        print(position)
        print("+"*50)

if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()