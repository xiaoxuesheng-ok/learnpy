#!/user/bin/python
# coding:UTF-8

import requests
from bs4 import BeautifulSoup # 从BS4这个库导图BrautifulSoup

link = "http://www.santostang.com"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

r = requests.get(link,headers = headers)

soup = BeautifulSoup(r.text,"lxml")  #使用BeautifulSoup解析这段代码

title = soup.find("h1",class_="post-title").a.text.strip()

with open('title.txt',"a+") as f:
    f.write(title)
    f.close()
