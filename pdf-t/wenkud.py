#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib.request
from urllib.parse import quote

import re
import requests
import os
import os.path



def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html

def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = url_re.findall(html.decode('gb2312'))
    return(url_lst)



def down_file(url,filk_path):
    try:
        res = requests.get(url, stream=True)
    except:
        return
    f = open(filk_path,'wb')
    for chunk in res.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            f.flush()
    f.close()





if __name__ == '__main__':
    raw_url = "https://www.google.co.jp/search?q=allinurl:+pdf+filetype:pdf&ei=M93cWZvYNcTOmwHBgJngDg&start=0&sa=N&biw=1440&bih=769"
    html = getHtml(raw_url)
    url_lst = getUrl(html)

    os.mkdir('ldf_download')
    os.chdir(os.path.join(os.getcwd(), 'ldf_download'))



