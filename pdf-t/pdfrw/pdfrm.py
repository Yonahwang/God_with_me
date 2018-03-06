#!/usr/bin/python
# -*- coding: utf-8 -*-

from pdfrw import PdfReader
x = PdfReader('/home/yonah/PDFdata/filevirus-noParse/VirusShare_fff35faf8ae0ede981413ec7e156685e')
x.keys()
#['/Info', '/Size', '/Root']
x.Info
# {'/Producer': '(cairo 1.8.6 (http://cairographics.org))',
# '/Creator': '(cairo 1.8.6 (http://cairographics.org))'}
x.Root.keys()
#['/Type', '/Pages']

