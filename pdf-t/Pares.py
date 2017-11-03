#!/usr/bin/python
# -*- coding: utf-8 -*-


import pdfid
import re



def id(pdf):
    try:
        # (dir, allNames, extraData, disarm, force), force)
        command = pdfid.PDFiD2String(pdfid.PDFiD(pdf, True, True, False, True), True)
        extra = True
    except Exception:
        # I've observed some files raising errors with the 'extraData' switch
        command = pdfid.PDFiD2String(pdfid.PDFiD(pdf, True, False, False, True), True)
        print "[!] PDFiD couldn\'t parse extra data"
        extra = False

    for line in command.split('\n'):
        count = re.split(r'[\s]+', line)
        if "PDF Header" in line and not re.match('%PDF-1\.\d', count[3]):
            counter.append("header")
            print "[-] Invalid version number : \"%s\"" % count[3]
        elif "/Page " in line:
            page_counter.append(count[2])
        elif "/Pages " in line:
            page_counter.append(count[2])
        elif "/JS " in line and not re.match('0', count[2]):
            counter.append("js")
            print "[-] JavaScript count.......: %s" % count[2]
            if count[2] > "1":
                counter.append("mucho_javascript")
                print "\t[*] That\'s a lot of js ..."
        elif "/AcroForm " in line and not re.match('0', count[2]):
            counter.append("acroform")
            print "[-] AcroForm...............: %s" % count[2]
        elif "/AA " in line and not re.match('0', count[2]):
            counter.append("aa")
            print "[-] Additional Action......: %s" % count[2]
        elif "/OpenAction " in line and not re.match('0', count[2]):
            counter.append("oa")
            print "[-] Open Action............: %s" % count[2]
        elif "/Launch " in line and not re.match('0', count[2]):
            counter.append("launch")
            print "[-] Launch Action..........: %s" % count[2]
        elif "/EmbeddedFiles " in line and not re.match('0', count[2]):
            counter.append("embed")
            print "[-] Embedded File..........: %s" % count[2]
        # elif "trailer" in line and not re.match('0|1', count[2]):
        #    print "[-] Trailer count..........: %s" % count[2]
        #    print "\t[*] Multiple versions detected"
        elif "Total entropy:" in line:
            tentropy = count[3]
            print "[-] Total Entropy..........: %7s" % count[3]
        elif "Entropy inside streams:" in line:
            ientropy = count[4]
            print "[-] Entropy inside streams : %7s" % count[4]
        elif "Entropy outside streams:" in line:
            oentropy = count[4]
            print "[-] Entropy outside streams: %7s" % count[4]

    if not extra == False:
        te_long = Decimal(tentropy)
        te_short = Decimal(tentropy[0:3])
        ie_long = Decimal(ientropy)
        ie_short = Decimal(ientropy[0:3])
        oe_long = Decimal(oentropy)
        oe_short = Decimal(oentropy[0:3])
        ent = (te_short + ie_short) / 2
        # I know 'entropy' might get added twice to the counter (doesn't matter) but I wanted to separate these to be alerted on them individually
        togo = (8 - oe_long)  # Don't want to apply this if it goes over the max of 8
        if togo > 2:
            if oe_long + 2 > te_long:
                counter.append("entropy")
                print "\t[*] Entropy of outside stream is questionable:"
                print "\t[-] Outside (%s) +2 (%s) > Total (%s)" % (oe_long, oe_long + 2, te_long)
        elif oe_long > te_long:
            counter.append("entropy")
            print "\t[*] Entropy of outside stream is questionable:"
            print "\t[-] Outside (%s) > Total (%s)" % (oe_long, te_long)
        if str(te_short) <= "2.0" or str(ie_short) <= "2.0":
            counter.append("entropy")
            print "\t[*] LOW entropy detected:"
            print "\t[-] Total (%s) or Inside (%s) <= 2.0" % (te_short, ie_short)

    # Process the /Page(s) results here just to make sure they were both read
    if re.match('0', page_counter[0]) and re.match('0', page_counter[1]):
        counter.append("page")
        print "[-] Page count suspicious:"
        print "\t[*] Both /Page (%s) and /Pages (%s) = 0" % (page_counter[0], page_counter[1])
    elif re.match('0', page_counter[0]) and not re.match('0', page_counter[1]):
        counter.append("page")
        print "[-] Page count suspicious, no individual pages defined:"
        print "\t[*] /Page = (%s) , /Pages = (%s)" % (page_counter[0], page_counter[1])
    elif re.match('1$', page_counter[0]):
        counter.append("page")
        print "[-] (1) page PDF"














