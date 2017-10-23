#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
#from peepdf.PDFCore import PDFParser
from peepdf.PDFCore import *

#file = r"F:\PDFdata\VirusShare_PDF_20170404\VirusShare_7df9eb586976d29892dda61823b7cbcc"
file = r"/home/yonah/PDFdata/malPDF/VirusShare_7b20cf0d3864b970ee92db3cf61938cf"


# bool change to string
def bool_change(vlue):
    if vlue == True:
        return 0
    else:
        return 1


#判断是否为PDF文件
def feature_extract(froot): #对输入文件进行特征提取
    '''***********************'''
    feature = dict()
    f_id = []
    pdfParser = PDFParser()
    _, pdf = pdfParser.parse(froot)
    statsDict = pdf.getStats()
    for version in range(len(statsDict['Versions'])):
        statsVersion = statsDict['Versions'][version]


        Actions = statsVersion['Actions']
        Events = statsVersion['Events']
        vulns = statsVersion['Vulns']
        elements = statsVersion['Elements']
        Catalog = statsVersion['Catalog']
        print Actions,Events,vulns,elements,Catalog



    feature['version'] = pdf.version
    feature['num_stream'] = pdf.numStreams
    feature['file_size'] = pdf.getSize()
    feature['num_object'] = pdf.numObjects
    feature['update'] = pdf.getNumUpdates()
    feature['comments'] = len(pdf.comments)
    feature['error'] = len(pdf.errors)
    feature['len_URLs'] = len(pdf.getURLs())
    feature['Binary'] = bool_change(statsDict['Binary'])
    feature['Linearized'] = bool_change(statsDict['Linearized'])
    feature['Encrypted'] = bool_change(statsDict['Encrypted'])
    feature['Catalog'] = statsDict['Catalog']

    for i in feature:
        f_id.append(i)

    for k in feature:
        print(k,feature[k])
    #print('fileneme: %s'%name)

    return [feature[k] for k in feature],f_id



if __name__ == '__main__':
    print feature_extract(file)
