'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/12 9:22
@Software: PyCharm
@File    : lagou1.py
'''
import requests
from lxml import etree
import time
import json
import re

start_url = "https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC"
url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400',
}
data = {
    'first': 'true',
    'pn':'1',
    'kd': 'python'
}
def parse_list_page():
    for x in range(1, 3):
        print(x)
        data['pn'] = str(x)
        s = requests.Session()
        s.get(start_url, headers=headers, timeout=3)  # 请求首页获取cookies
        cookie = s.cookies  # 为此次获取的cookies
        response = requests.post(url=url, headers=headers, data=data,
                                 cookies=cookie, timeout=3)
        # print(type(response.json()))
        print(response.text)
        # print(response.json())#json方法，将json数据load成一个字典
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionId = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' %positionId
            print(position_url)
            parse_position_detail(position_url)
            break
        break
        # time.sleep(4)#防止爬取频繁

def parse_position_detail(url):
    response = requests.get(url,headers=headers)
    # print(response.text)
    text = response.text
    html = etree.HTML(text)
    position_name = html.xpath("//span[@class='name']/text()")[0]
    print(position_name)
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath('.//text()')[0].strip()
    print(salary)
    city = job_request_spans[1].xpath('.//text()')[0].strip()
    city = re.sub(r'[\s/]','',city)
    print(city)
    work_years = job_request_spans[2].xpath('.//text()')[0].strip()
    work_years = re.sub(r'[\s/]','',work_years)
    print(work_years)
    education = job_request_spans[3].xpath('.//text()')[0].strip()
    education = re.sub(r'[\s/]','',education)
    print(education)
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()#join()将列表转换为字符串
    print(desc)

def main():
    parse_list_page()


if __name__ == '__main__':
    main()
