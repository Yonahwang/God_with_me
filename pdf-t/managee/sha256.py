#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import os


#files =r"/home/yonah/PDFdata/pdfnormal"
files = r"/home/yonah/Data/mal2k"
pathDir =  os.listdir(files)

#downf = open("tsha1.txt",'wb')
f = open("tsha1.txt",'wb')
file_sha256 = []
for file in pathDir:
    f = files + "/" + file
    fr = open(f, 'rb')
    sh = hashlib.sha256()
    sh.update(fr.read())
    file_sha256.append(sh.hexdigest())
    f.write(file_sha256,'a')



f.close()


