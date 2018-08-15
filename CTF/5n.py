#!/usr/bin/python
# -*- coding: utf-8 -*-

a = 'afZ_r9VYfScOeO_UL^RWUc'
ctf = ''
i= 5
for s in a:
    r = ord(s) + i
    ctf += chr(r)
    i = i+1
print(ctf)



