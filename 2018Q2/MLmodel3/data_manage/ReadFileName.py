#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os
import pickle

file_p = "/home/yonah/data/PDFdata/mal2k/"

def main():
    print 'start...........'

    #file_path = sys.argv[1]
    #files = []
    pathDir = os.listdir(file_p)

    file_name = []
    output = open("mal2k.txt", 'wb')

    for file in pathDir:
        file_path = file_p + file
        #file_name.append(file_path)
        output.write(file_path)
        output.write("\n")
    pickle.dump(file_name, output)




if __name__ == "__main__":
    main()