#!/usr/bin/env python
#encoding=utf-8
import requests
from  bs4 import BeautifulSoup
url = 'https://www.zhihu.com/hot'
headers ={
    "hosts":"www.zhihu.cm",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0",
}
html = requests.get(url,verify = False).content.decode('utf-8') # verify = False表示请求https
soup = BeautifulSoup(html,'html.parser')
name = soup.find_all('a',target="_blank")
for i in name:
    print(i)