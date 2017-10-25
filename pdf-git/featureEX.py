# -*- coding: utf-8 -*-
# !/usr/bin/python
from peepdf.PDFCore import *

def fakeFile_check(filePath):
    try:
        from peepdf.PDFCore import PDFParser
        pdfParser = PDFParser()
        _, pdf = pdfParser.parse(filePath)
        return pdf
    except Exception:
        return None

# bool change to string
def bool_change(vlue):
    if vlue == True:
        return 0
    else:
        return 1


def None_int(vlue):
    if vlue == None:
        return 0
    else:
        return int(vlue[0])

def None_len(vlue):
    if vlue == None:
        return 0
    else:
        return len(vlue)

def None_vlue(vlue):
    if vlue == None:
        return 0
    else:
        return vlue


def feature_extract(pdf):  # 对输入文件进行特征提取

    feature = dict()
    f_id = []
    statsDict = pdf.getStats()
    gtree = pdf.getTree()

    feature['JS_MODULE'] = bool_change(JS_MODULE)
    font_count = 0
    Javascript_count = 0
    JS_count = 0
    acd = gtree[len(gtree) - 1][1]
    for k in acd:
        if '/Font' == acd[k][0]:
            font_count += 1
        if '/JavaScript' == acd[k][0]:
            Javascript_count += 1
        if '/JS' == acd[k][0]:
            JS_count += 1
    feature['font_count'] = font_count
    feature['Javascript_count'] = Javascript_count
    feature['JS_count'] = JS_count

    for version in range(len(statsDict['Versions'])):
        statsVersion = statsDict['Versions'][version]
        obj = []
        obj_size = []

        for ob in statsVersion['Objects'][1]:
            obj_one = pdf.getObject(ob).getValue()
            obj.append(obj_one)
            obj_size.append(len(obj_one))
        obj_size.sort(cmp=None, key=None, reverse=True);  # 对这个存有10个最大值数组（TopK数组）进行降序排序
        if len(obj_size) >= 10:
            for h in range(10):
                feature['obj_10_' + str(h)] = obj_size[h]
        else:
            while 10-len(obj_size)> 0:
                obj_size.append(0)
            for h in range(10):
                feature['obj_10_' + str(h)] = obj_size[h]

        feature['Catalog'] = None_vlue(statsVersion['Catalog'])
        feature['Xref Streams'] = None_int(statsVersion['Xref Streams'])
        feature['elements'] = None_len(statsVersion['Elements'])
        feature['Events_num'] = None_len(statsVersion['Events'])
        feature['Actions_num'] = None_len(statsVersion['Actions'])
        feature['Vulns'] = None_len(statsVersion['Vulns'])
        feature['Encoded_num'] = None_int(statsVersion['Encoded'])
        feature['Objects_JS_num'] = None_int(statsVersion['Objects with JS code'])
        feature['Compressd_obj'] = None_int(statsVersion['Compressed Objects'])
        feature['Xref Streams'] = None_int(statsVersion['Xref Streams'])
        feature['Info'] = None_int(statsVersion['Info'])
        feature['Object Streams'] = None_int(statsVersion['Object Streams'])
        #feature['Decoding Errors'] = None_int(statsVersion['Decoding Errors'])

    '''sha1 = pdf.getSHA1()
    for h in range(len(sha1)):
        feature['sha1_' + str(h)] = int(sha1[h], 16)
    md5 = pdf.getMD5()
    for g in range(len(md5)):
        feature['md5_' + str(g)] = int(md5[g], 16)'''

    feature['Binary'] = bool_change(statsDict['Binary'])
    feature['Linearized'] = bool_change(statsDict['Linearized'])
    feature['Encrypted'] = bool_change(statsDict['Encrypted'])
    feature['Metadata'] = None_len(pdf.getMetadata())
    feature['version'] = pdf.version
    feature['stream_num'] = pdf.numStreams
    feature['file_size'] = pdf.getSize()
    feature['object_num'] = pdf.numObjects
    feature['update'] = pdf.getNumUpdates()
    feature['comments'] = len(pdf.comments)
    feature['error'] = len(pdf.errors)
    feature['len_URLs'] = len(pdf.getURLs())

    for i in feature:
        f_id.append(i)




    return [feature[k] for k in feature],f_id