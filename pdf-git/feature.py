from peepdf.PDFCore import *
pdfParser = PDFParser()

#feature_extract
class featureEX:


    def fakeFile_check(filePath):

        try:

            _, pdf = pdfParser.parse(filePath)
            return pdf
        except Exception:
            return None

    def feature_extract(pdf):  #对输入文件进行特征提取

        '''***********************'''
        feature = dict()
        statsDict = pdf.getStats
        md5 = pdf.getMD5()
        for g in range(len(md5)):
            feature['md5_'+ str(g)] = int(md5[g],16)
        version =pdf.getVersion()
        feature['ver'] = float(version)
        feature['numstream'] = pdf.numStreams
        feature['size'] = pdf.getSize()
        feature['numofobject'] = pdf.numObjects
        feature['update'] = pdf.getNumUpdates()
        feature['comments'] = len(pdf.comments)
        feature['error'] = len(pdf.errors)

        print('OK')

        return [feature[k] for k in feature]