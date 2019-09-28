'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/16 9:50
@Software: PyCharm
@File    : boss.py
'''
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
import time
import csv
import pytesseract
from urllib import request
from PIL import Image


class BossSpider(object):
    driver_path = r'C:\geckodriver\geckodriver.exe'
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=BossSpider.driver_path)
        self.url = "https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position="
        # self.positions = []
        self.domain = "https://www.zhipin.com"
        pytesseract.pytesseract.tesseract_cmd = r"C:\TesseractOCR\tessract.exe"
        fp = open('boss.csv','a',newline='',encoding='utf-8')
        self.writer = csv.DictWriter(fp,[ 'name','company_name','salary','city','work_years','education','desc'])
        self.writer.writeheader()

    def run(self):
        self.driver.get(self.url)
        while True:
            # if len(self.driver.find_element_by_id("captcha"))>0:
            #     self.fill_captcha()
            #     time.sleep(2)
            #     continue
            source = self.driver.page_source
            # print(source)
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(@class,'next')]"))
            )
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath("//a[contains(@class,'next')]")
            if "disabled" in next_btn.get_attribute('class'):
                break
            else:
                next_btn.click()

    def fill_captcha(self):
        captchaInput = self.driver.find_element_by_id("captcha")
        captchaImg = self.driver.find_element_by_class_name("code")
        submitBtn = self.driver.find_element_by_class_name("btn")
        src = captchaImg.get_attribute("src")
        request.urlretrieve(self.domain + src,"captcha.png")
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        captcha = re.sub(r"[\s/]","",text)
        captchaInput.send_keys(captcha)
        submitBtn.click()

    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//div[@class='info-primary']//a[position()]/@href")
        for link in links:
            url = self.domain + link
            print(url)
            # self.driver.get(url)
            # source1 = self.driver.page_source
            # print(source1)

            self.request_detail_page(url)
            time.sleep(1)
            break

    def request_detail_page(self,url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='job-box']//div[@class='job-detail']"))
        )
        source = self.driver.page_source
        # print(source)
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        # print(html)
        position_name = html.xpath("//div[@class='name']/h1/text()")[0].strip()
        # print(position_name)
        company_name = html.xpath('//div[@class="company-info"]//a[@ka="job-detail-company"]/text()')[2].strip()
        print(company_name)
        salary = html.xpath('//div[@class="name"]/span[@class="salary"]/text()')[0].strip()
        # print(salary)
        infos = html.xpath('//div[@class="job-primary detail-box"]//div[@class="info-primary"]//p/text()')
        city = infos[0]
        # print(city)
        work_years = infos[1]
        # print(work_years)
        education = infos[2]
        # print(education)
        desc = "\n".join(html.xpath("//div[@class='job-sec']/div[@class='text']//text()")).strip()  # join()将列表转换为字符串
        # print(desc)
        position = {
            'name': position_name,
            'company_name': company_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'desc': desc
        }
        # self.positions.append(position)
        print(position)
        # self.write_position(position)

    def write_position(self,position):
        self.writer.writerow(position)
        print(position)

if __name__ == '__main__':
    spider = BossSpider()
    spider.run()
