#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import os
import sys
import pickle

'''files = r"/home/yonah/PDFdata/filevirus-noParse"
pathDir =  os.listdir(files)
downf = open("tsha1.txt",'wb')
file_sha256 = []
for file in pathDir:
    f = files + "/" + file
    fr = open(f, 'rb')
    sh = hashlib.sha1()
    sh.update(fr.read())
    file_sha256.append(sh.hexdigest())
    downf.write(sh.hexdigest() + '\n')

#pickle.dump(file_sha256,open('pdf_sha256.pkl','wb'))

downf.close()'''

def main():
    print 'start...........'

    file_path = sys.argv[1]
    #files = []
    pathDir = os.listdir(file_path)
    downf = open("sha245.txt", 'wb')
    file_sha256 = []
    for file in pathDir:
        f = file_path + "/" + file
        fr = open(f, 'rb')
        sh = hashlib.sha1()
        sh.update(fr.read())
        file_sha256.append(sh.hexdigest())
        downf.write(sh.hexdigest() + '\n')
    pickle.dump(file_sha256, open('pdf_sha256.pkl', 'wb'))
    downf.close()

    #print 'A total of %d files got sha256 ' % (len(files))


if __name__ == "__main__":
    main()