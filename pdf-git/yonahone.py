#!/usr/bin/python
# -*- coding: utf-8 -*-


import re

#from peepdf.PDFCore import PDFParser
from peepdf.PDFCore import *
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

#file = r"/Users/fengjiaowang/Downloads/data2000/pdf/0058a8ee044b833b4d0cee9993cb4175f145075c.pdf"
file = r"/Users/fengjiaowang/Downloads/data2000/VirusS/VirusShare_00a0e3c78ac85866d0349d2d8e1f57e0"
#file = r"/home/yonah/PDFdata/malPDF/VirusShare_ffc1941e3eb5c85cabf6eea94d742b0e"
#file = r"/home/yonah/PDFdata/pdfnormal/SQL_tutorial_pt1.pdf"



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

def YESorNO(vlue):
    if len(vlue) != 0:
        return len(vlue)
    else:
        return 0

def exist(vl):
    if vl:
        return vl
    else:
        return 0


#判断是否为PDF文件
def feature_extract(froot): #对输入文件进行特征提取
    '''***********************'''
    feature = dict()
    f_id = []
    pdfParser = PDFParser()
    _, pdf = pdfParser.parse(froot)
    statsDict = pdf.getStats()






    trailer = pdf.getTrailer()
    if trailer[0] == 0:
        feature['trailer_num'] = 0
    elif trailer[0] != 0:
        feature['trailer_num'] = trailer[0]

    XrefSection = pdf.getXrefSection()
    feature['XrefSection'] = len(XrefSection)
    Xref = XrefSection[1][0]
    if Xref != None:
        feature['Xref_size'] = Xref.size
        feature['Xref_stream'] = None_int(Xref.streamObject)
        feature['Xref_offset'] = Xref.offset
        feature['Xref_bytesPerFisId'] = len(Xref.bytesPerField)
        feature['Xref_errors'] = len(Xref.errors)
        subsections = XrefSection[1][0].subsections[0]
        if subsections != None:
            feature['subsections_size'] = subsections.size
            feature['subsections_numObjects'] = subsections.numObjects
            feature['subsections_firstObject'] = subsections.firstObject
            feature['subsections_offset'] = subsections.offset
            feature['subsections_entries'] = len(subsections.entries)
            feature['subsections_errors'] = len(subsections.errors)
        if subsections == None:
            feature['subsections_size'] = 0
            feature['subsections_numObjects'] = 0
            feature['subsections_firstObject'] = 0
            feature['subsections_offset'] = 0
            feature['subsections_entries'] = 0
            feature['subsections_errors'] = 0

    elif Xref == None:
        feature['Xref_size'] = 0
        feature['Xref_stream'] = 0
        feature['Xref_offset'] = 0
        feature['Xref_bytesPerFisId'] = 0
        feature['Xref_errors'] = 0
        if XrefSection[1][1] != None:
            subsections = XrefSection[1][1].subsections[0]
            if subsections != None:
                feature['subsections_size'] = subsections.size
                feature['subsections_numObjects'] = subsections.numObjects
                feature['subsections_firstObject'] = subsections.firstObject
                feature['subsections_offset'] = subsections.offset
                feature['subsections_entries'] = len(subsections.entries)
                feature['subsections_errors'] = len(subsections.errors)
            if subsections == None:
                feature['subsections_size'] = 0
                feature['subsections_numObjects'] = 0
                feature['subsections_firstObject'] = 0
                feature['subsections_offset'] = 0
                feature['subsections_entries'] = 0
                feature['subsections_errors'] = 0
        if XrefSection[1][1] == None:
            feature['subsections_size'] = 0
            feature['subsections_numObjects'] = 0
            feature['subsections_firstObject'] = 0
            feature['subsections_offset'] = 0
            feature['subsections_entries'] = 0
            feature['subsections_errors'] = 0


    Header = pdf.getHeaderOffset()
    #getVarContent()
   # PDFBody.containsXrefStreams(pdf)

    JavascriptCode = pdf.getJavascriptCode()
    Offsets = pdf.getOffsets()
    Catalog = pdf.getCatalogObjectId()

    print pdf.getEndLine()
    # print pdf.maxObjectId






    Metadata = pdf.getBasicMetadata(0)
    feature['Metadata_len'] = None_len(Metadata)
    meta_creation = ''
    meta_producer = ''
    meta_creator = ''
    meta_author = ''
    for k in Metadata:
        if k == 'creation':
            meta_creation = Metadata[k]
        elif k == 'producer':
            meta_producer = Metadata[k]
        elif k == 'creator':
            meta_creator = Metadata[k]
        elif k == 'author':
            meta_author = Metadata[k]
    feature['meta_cration_len'] = YESorNO(meta_creation)
    feature['meta_producer_len'] = YESorNO(meta_producer)
    feature['meta_creator_len'] = YESorNO(meta_creator)
    feature['meta_author_len'] = YESorNO(meta_author)

    '''if len(meta_creation) !=0:
        timeC = meta_creation[2:16]
        feature['meta_creation'] = meta_creation[2:16]
    else:
        feature['meta_creation'] = '''


    gtree = pdf.getTree()
    font_count = 0
    Javascript_count = 0
    JS_count = 0
    acd = gtree[len(gtree)-1][1]
    feature['tree_len'] = len(acd)
    for k in acd:
        if '/Font'== acd[k][0]:
            font_count += 1
        if '/JavaScript'== acd[k][0]:
            Javascript_count += 1
        if '/JS' == acd[k][0]:
            JS_count += 1
    feature['font_count'] = font_count
    feature['Javascript_count'] = Javascript_count
    feature['JS_count'] = JS_count



    feature['JS_MODULE'] = bool_change(JS_MODULE)
    #feature['MAL_ALL']= MAL_ALL
    #feature['MAL_BAD_HEAD'] = MAL_BAD_HEAD
    #feature['MAL_EOBJ'] = MAL_EOBJ
    #feature['MAL_ESTREAM'] = MAL_ESTREAM
    #feature['MAL_HEAD'] = MAL_HEAD
    #feature['MAL_XREF'] = MAL_XREF




    for version in range(len(statsDict['Versions'])):


        statsVersion = statsDict['Versions'][version]
        obj = statsVersion['Objects'][1]
        obj_size = []
        for ob in obj:
            obj_one = pdf.getObject(ob).getValue()
            obj_size.append(len(obj_one))
        obj_size.sort(cmp=None, key=None, reverse=True)  # 进行降序排序从大到小排序
        if len(obj_size) >= 10:
            for h in range(10):
                feature['obj_10_' + str(h)] = obj_size[h]
        else:
            while 10-len(obj_size)> 0:
                obj_size.append(0)
            for h in range(10):
                feature['obj_10_' + str(h)] = obj_size[h]

        stream = statsVersion['Streams'][1]
        stream_size = []
        for s in stream:
            stream_one = pdf.getObject(s).getValue()
            stream_size.append(len(stream_one))
        stream_size.sort() #从小到大排序
        if len(stream_size) >= 2:
            for h in range(2):
                feature['stream_min_' + str(h)] = stream_size[h]
        else:
            while 2-len(stream_size) >0:
                stream_size.append(0)
            stream_size.sort()
            for h in range(2):
                feature['stream_min_' + str(h)] = stream_size[h]

        feature['Catalog'] = None_vlue(statsVersion['Catalog'])
        feature['Xref Streams'] = None_int(statsVersion['Xref Streams'])
        feature['elements'] = None_len(statsVersion['Elements'])
        feature['Events_num'] = None_len(statsVersion['Events'])
        feature['Actions_num'] = None_len(statsVersion['Actions'])
        feature['Vulns'] = None_len(statsVersion['Vulns'])
        feature['Encoded_num'] = None_int(statsVersion['Encoded'])
        feature['Objects_JS_num'] = None_int(statsVersion['Objects with JS code'])
        feature['Compressd_obj'] = None_int(statsVersion['Compressed Objects'])
        feature['Info'] = None_int(statsVersion['Info'])
        feature['Object Streams'] = None_int(statsVersion['Object Streams'])
        #feature['Decoding Errors'] = None_int(statsVersion['Decoding Errors'])  #error


    feature['Binary'] = bool_change(statsDict['Binary'])
    feature['Linearized'] = bool_change(statsDict['Linearized'])
    feature['Encrypted'] = bool_change(statsDict['Encrypted'])
    feature['version'] = pdf.version
    feature['stream_num'] = pdf.numStreams
    feature['file_size'] = pdf.getSize()
    feature['object_num'] = pdf.numObjects
    feature['update'] = pdf.getNumUpdates()
    feature['comments'] = len(pdf.comments)
    feature['error'] = len(pdf.errors)
    feature['len_URLs'] = len(pdf.getURLs())
    feature['numEncodedStreams'] = pdf.numEncodedStreams
    #feature['Catalog_id'] = pdf.getCatalogObjectId() #[int,None]
    feature['header_offset'] = pdf.getHeaderOffset()

    '''sha1 = pdf.getSHA1()
    for h in range(len(sha1)):
        feature['sha1_' + str(h)] = int(sha1[h], 16)'''
    for i in feature:
        f_id.append(i)

    #test
    for k in feature:
        print(k,feature[k])
    #print('fileneme: %s'%name)
    print len(feature)

    return [feature[k] for k in feature],f_id



if __name__ == '__main__':
    feature_extract(file)

