#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import os
import pickle

#files =r"/home/yonah/PDFdata/pdfnormal"
files = r"/home/yonah/Data/mal2k"
pathDir =  os.listdir(files)

#downf = open("tsha1.txt",'wb')
file_sha256 = []
for file in pathDir:
    f = files + "/" + file
    fr = open(f, 'rb')
    sh = hashlib.sha256()
    sh.update(fr.read())
    file_sha256.append(sh.hexdigest())
#    downf.write(sh.hexdigest() + '\n')
output = open("tsha1.txt",'wb')

#pickle.dump(file_sha256)
pickle.dump(file_sha256, output)

output.close()

