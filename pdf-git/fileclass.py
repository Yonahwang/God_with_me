# -*- coding: utf-8 -*-
# !/usr/bin/python

# 导入需要用到的库

import os
from peepdf.PDFCore import PDFParser
import shutil



# 全局参数配置，根据需要自己修改以下六个参数
file_root = r"/home/yonah/PDFdata/Virus15K/" # 正常样本数据集的文件路径


def get_data(f_list):
     for i in f_list:
        T_file = file_root + i
        pdfParser = PDFParser()
        try:
            _, pdf = pdfParser.parse(T_file)
            #newfile = os.getcwd() + '/' + file_classify
            #shutil.copytree(file_root+i, newfile+i)   #复制文件到新文件夹  ，移动用move

        except Exception:
            newfile = r'/home/yonah/PDFdata/filevirus-noParse/'
            print i
            shutil.copy(T_file, newfile+i)   #复制文件到新文件夹  ，移动用move
            #print i
            continue

    return newfile

def  get_count(path):
    count = 0
    for root, dirs, files in os.walk(path):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
    print count  # 输出结果


if __name__ == '__main__':
    print('start processing')
    #file_classify = 'filevirus/'
    #if not os.path.exists(file_classify):  # 判断文件夹是否存在
        #os.mkdir('filevirus')

    file_list = os.listdir(file_root)  # 列出文档
    get_data(file_list)

    #count = 0
    #for root, dirs, files in os.walk(path):  # 遍历统计
        #for each in files:
            #count += 1  # 统计文件夹下文件个数
    #print count  # 输出结果

