# -*- coding: utf-8 -*-
# !/usr/bin/python


def fakeFile_check(filePath):
    try:
        from peepdf.PDFCore import PDFParser
        pdfParser = PDFParser()
        _, pdf = pdfParser.parse(filePath)
        return pdf
    except Exception:
        return None


def feature_extract(pdf):  # 对输入文件进行特征提取

    '''***********************'''


    feature = dict()
    f_id = []
    statsDict = pdf.getStats
    name = pdf.getFileName()
    md5 = pdf.getMD5()
    for g in range(len(md5)):
        feature['md5_' + str(g)] = int(md5[g], 16)

    sha1 = pdf.getSHA1()
    '''for h in range(len(sha1)):
        feature['sha1_' + str(h)] = int(sha1[h], 16)
    sha256 = pdf.getSHA256()
    for s in range(len(sha256)):
        feature['sha256_' +str(s) ] = int(sha256[s],16)'''
    version = pdf.getVersion()
    feature['ver'] = float(version)
    feature['numstream'] = pdf.numStreams
    feature['size'] = pdf.getSize()
    feature['numofobject'] = pdf.numObjects
    feature['update'] = pdf.getNumUpdates()
    feature['comments'] = len(pdf.comments)
    feature['error'] = len(pdf.errors)

    for i in feature:
        f_id.append(i)


    #print('fileneme: %s'%name)

    return [feature[k] for k in feature],f_id