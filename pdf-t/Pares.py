#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import datetime
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import matplotlib.pyplot as plt
import numpy as np

#获取文档路径，
file_path = r"F:/PDFdata/small_202/normalpdf"

def get_time(file):
    # 创建一个与文档相关联的解释器
    parser = PDFParser(file)

    # PDF文档对象
    doc = PDFDocument(parser)

    timedict = doc.info[0]
    time = timedict['ModDate']
    return time

# 载入数据集
def load_file(PEfile_Path):
    test_files = list()
    for dirpath, dirname, filenames in os.walk(PEfile_Path):
        for filename in filenames:
            rfpath = dirpath + "/"+ filename
            test_files.append(rfpath)
    return test_files

def get_years(file_path):
    pdf_path = load_file(file_path)
    nor_time = list()
    for fileone in pdf_path:
        try:
            fp = open(fileone , "rb")
            time = get_time(fp)
            t3 = time [:2]
            if time[:2] == "D:":
                year = time[2:6]
                nor_time.append(year)

        except Exception as e:
            #print('file %s feature extracting meet ERROR' % fp)
            #print(e)
            continue
    return nor_time

def data_Statistics(list):
    t_num = {}
    for i in list:
        t_num[i] = list.count(i)

    t_year = list()
    num = list()
    for i in t_num:
        t_year.append(i)
        num.append(t_num[i])
    y = num
    index = t_year
    plt.bar(left=index, height=y, color='green', width=0.5)
    plt.show()

    return t_num




if __name__ == '__main__':
    print "test......."
    start = datetime.datetime.now()
    year = get_years(file_path)
    num = data_Statistics(year)
    print num
    end = datetime.datetime.now()






