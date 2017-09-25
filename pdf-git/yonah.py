



import subprocess
from peepdf.PDFCore import PDFParser




def getpdfhear():
    pass


if __name__ == '__main__':

    #cmd ='python peepdf/peepdf.py /Users/fengjiaowang/Desktop/yonah/cve2010-2883.pdf'
    #subprocess.call(cmd,shell=True)
    pdfParser = PDFParser()
    ret, pdf = pdfParser.parse('/Users/fengjiaowang/Desktop/yonah/cve2010-2883.pdf')
    statsDict = pdf.getStats
    tree = pdf.getTree()
    print tree
    print tree.get('/Catalog')

    #print pdf.getObject(10).getValue()
    #a = input()
    #pdf.close()
