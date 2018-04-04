#!/usr/bin/python
# -*- coding: utf-8 -*-


L = ['<a href="/cgi-bin/cvename.cgi?name=CVE-2004-0194">CVE-2004-0194</a>', '<a href="/cgi-bin/cvename.cgi?name=CVE-2003-0508">CVE-2003-0508</a>', '<a href="/cgi-bin/cvename.cgi?name=CVE-2003-0434">CVE-2003-0434</a>', '<a href="/cgi-bin/cvename.cgi?name=CVE-2003-0284">CVE-2003-0284</a>', '<a href="/cgi-bin/cvename.cgi?name=CVE-2003-0204">CVE-2003-0204</a>', '<a href="/cgi-bin/cvename.cgi?name=CVE-2003-0142">CVE-2003-0142</a>', '<a href="/cgi-bin/cvename.cgi?name=CVE-2002-1569">CVE-2002-1569</a>', '<a href="/cgi-bin/cvename.cgi?name=CVE-2002-0838">CVE-2002-0838</a>', '<a href="/cgi-bin/cvename.cgi?name=CVE-2002-0030">CVE-2002-0030</a>']

timm= []
for i in L :

    tim = i[-13:-9]
    timm.append(tim)

from collections import Counter
print Counter(timm)



