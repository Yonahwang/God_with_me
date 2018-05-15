#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys



def main():
    print 'start...........'

    file_path = sys.argv[1]
    liss= []
    for file in os.listdir(file_path):

        if file[-4:] != '.pdf':
            new_name = file + '.pdf'
            os.rename(file_path + '/'+ file, file_path + '/' + new_name)
            liss.append(file)
    print 'A total of %d files changed ' % (len(liss))




if __name__ == "__main__":
    main()