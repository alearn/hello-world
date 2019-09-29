#!/usr/bin/env python
#encoding=utf-8

import re
from bs4 import BeautifulSoup
import urllib.request
import requests
import random

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0'
    }
#url = 'http://www.htu.edu.cn/8954/list.htm'
url = 'https://haokan.baidu.com/videoui/page/pc/search?query=%E9%87%8F%E5%AD%90%E6%95%85%E4%BA%8B%E4%BC%9A%E4%B9%9D'
r = requests.get(url=url,headers=headers)
soup = BeautifulSoup(r.content,'lxml')
print (soup.prettify())
#print (soup.title)
#print (soup.title.string)
#news_div = soup.find(attrs={"class":"list_right"})
#news_a = news_div.findAll(attrs={"class":"Article_Title"})
#print (news_a)
#for news in news_a:
#    print (news.string)