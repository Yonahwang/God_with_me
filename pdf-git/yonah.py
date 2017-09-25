



from peepdf.PDFCore import PDFParser
#TODO: ADD function


def getpdfhear():
    pass

if __name__ == '__main__':

    # cmd = 'python peepdf/peepdf.py /Users/fengjiaowang/Desktop/yonah/cve2010-2883.pdf'
    # subprocess.call(cmd,shell=True)
    pdfParser = PDFParser()
    _, pdf = pdfParser.parse('/Users/fengjiaowang/Desktop/yonah/cve2010-2883.pdf')
    statsDict = pdf.getStats
    tree = pdf.getTree()
    version = pdf.getVersion()
    MD5 = pdf.getMD5()
    print"MD5:",MD5
    print "Version:",version
    print "Tree:",tree
    #print tree.get('/Catalog')


    #print pdf.getObject(10).getValue()
    #a = input()
    #pdf.close()
