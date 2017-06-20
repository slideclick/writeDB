# -*- coding: UTF-8 -*-
#python 3
import lxml.html
import requests
import datetime
import csv


url="http://www.sohu.com/" #'http://home.sina.com.cn' 55118885
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
    print(html,file=csvFile,end='')#这里存为文件，应该可以用npp和IE打开，而不是乱码。其hex进制值就是下面的urlopen.read()
tree=lxml.html.fromstring(html)
print (tree.find(".//title").text)
print (tree.find(".//title").text.encode('utf-8',errors='xmlcharrefreplace').decode('utf-8'))
#'surrogateescape'


from bs4 import BeautifulSoup as soup
result = requests.get(url)
page = result.text
doc = soup(page,"lxml")
print (doc.title.string)
print (doc.title.string.encode('gbk',errors='replace').decode('cp936'))


from urllib.request import urlopen
textPage = urlopen(             url)
#print(textPage.read())  #bytes you can see the utf-8 value 

