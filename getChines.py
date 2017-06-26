# -*- coding: UTF-8 -*-
#python 3 中文
import requests
from bs4 import BeautifulSoup

url= 'http://home.sina.com.cn' # "http://www.55118885.com/w/126911204.html"
headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Mozilla/5.0',
    }
)
result = requests.get(url, headers=headers)
html = result.text # content会是raw字节，这时对它decode可以是中文
bsObj = BeautifulSoup(html, "lxml")
content = bsObj.find("div", {"class":"art-content tmd-content"}).get_text()
bcontent = bytes(content, "UTF-8")
scontent = bcontent.decode("UTF-8")

#from urllib.request import urlopen
#textPage = urlopen(             url)
