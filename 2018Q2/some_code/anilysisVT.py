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

def get_ratio(info):
    regex = r'>Detection ratio:<[\s\S]*?>Analysis date:<'
    ratio_code = re.findall(regex,info)
    print str(ratio_code)
    ratio_str = re.findall(r".../...",str(ratio_code))
    ratio = ratio_str[1]
    print ratio
    return ratio



if __name__ == '__main__':
    tags = []
    file_name = []
    ratios = []
    '''file = files[0]
    f_name = pathf + "/" + file
    info = get_content(f_name)
    print get_ratio(info)'''

    df = DataFrame(columns=['file_name','tags','ratio'])
    for file in files:
        f_name = pathf + "/" + file
        info = get_content(f_name)
        ratios.append(get_ratio(info))
        file_name.append(f_name)
        tags.append(get_tags(info))
    df['file_name'] = file_name
    df['tags'] = tags
    df['ratio'] = ratios
    df.to_csv('tags_ratio.csv',index=False,sep=',')

