import requests
import json
import re
import sys
from bs4 import BeautifulSoup

# url = "https://club.jd.com/comment/productPageComments.action?productId=4728280&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1"
# info = requests.get(url)
# json_data =  json.loads(info.text)
# comments = json_data['comments']
# for d in comments:
#     print(d['content'])
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
      'Connection':'Keep-Alive',
      'Accept-Language':'zh-CN,zh;q=0.8',
      'Accept-Encoding':'gzip,deflate,sdch',
      'Accept':'*/*',
      'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',
      'Cache-Control':'max-age=0'
      }
 
        