# -*- coding: UTF-8 -*-
#python 3
import lxml.html
import requests
import datetime
import csv


url='http://home.sina.com.cn'
headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Mozilla/5.0',
    }
)#http://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python

result = requests.get(url, headers=headers)
html = result.text
#print(html)
with open(r'sina.html','w',encoding='utf-8') as csvFile:
    print(html,file=csvFile,end='')
tree=lxml.html.fromstring(html)
print (tree.find(".//title").text.encode('cp936',errors='xmlcharrefreplace').decode('cp936'))
#'surrogateescape'

import requests
from bs4 import BeautifulSoup as soup
result = requests.get(url)
page = result.text
doc = soup(page)
print (doc.title.string.encode('gbk',errors='replace').decode('cp936'))