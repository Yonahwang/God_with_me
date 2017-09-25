#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
#from peepdf.PDFCore import PDFParser
from peepdf.PDFCore import *

file = r"F:\PDFdata\VirusShare_PDF_20170404\VirusShare_7df9eb586976d29892dda61823b7cbcc"
#file = r"F:\PDFdata\small_data\normalpdf\003.PDF"

#判断是否为PDF文件
def feature_extract(froot): #对输入文件进行特征提取
    '''***********************'''
    feature = dict()
    pdfParser = PDFParser()
    _, pdf = pdfParser.parse(froot)
    statsDict = pdf.getStats
    md5 = pdf.getMD5()
    for g in range(len(md5)):
        feature['md5_'+ str(g)] = int(md5[g],16)
    version =pdf.getVersion()
    feature['ver'] = float(version)
    feature['numstream'] = pdf.numStreams
    feature['size'] = pdf.getSize()
    feature['numofobject'] = pdf.numObjects
    feature['update'] = pdf.getNumUpdates()
    feature['comments'] = len(pdf.comments)
    feature['error'] = len(pdf.errors)
    for k in feature:
        print(k,feature[k])
    return [feature[k] for k in feature]



if __name__ == '__main__':
    print feature_extract(file)