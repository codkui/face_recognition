# -*- coding: UTF-8 -*-
from urllib import request
import chardet

def get(url,type=False):
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    if type==False:
        html=chardet.detect(html)
    return html
if __name__ == "__main__":
    
    print(html)