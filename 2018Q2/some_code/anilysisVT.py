#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import urllib
import re
from pandas import DataFrame

pathf = '/home/yonah/Data/vt_report_pdf'
files = os.listdir(pathf)

def get_content(html_page):
    '''html downladd'''
    html = urllib.urlopen(html_page)
    content = html.read()
    html.close()
    return content

def get_tags(info):
    '''html parser'''
    regex = r'>Tags<[\s\S]*?style=' # download original picture
    Tags_code =re.findall(regex,info)
    if len(Tags_code) != 0:
        tags = re.findall(r"label-info\">(.*?)</span>",Tags_code[0])
    else:
        tags = 0
    return tags

def Download_image():
    ''' image download'''
    for image_url in get_tags(info):
        print image_url
        image_name = image_url.split('/')[-1]
        # 给文件命名
        urllib.urlretrieve(image_url,image_name)



if __name__ == '__main__':
    tags = []
    file_name = []
    df_tags = DataFrame(columns=['file_name','tags'])
    for file in files:
        f_name = pathf + "/" + file
        info = get_content(f_name)
        tag = get_tags(info)
        if tag != 0:
            file_name.append(f_name)
            tags.append(tag)
    df_tags['file_name'] = file_name
    df_tags['tags'] = tags
    print tags