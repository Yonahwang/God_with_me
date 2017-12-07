# -*- coding: utf-8 -*-
#!/usr/bin/python

from __future__ import print_function
import sys
import os
from pyspark import SparkContext,SparkConf
from pyspark.mllib.regression import LabeledPoint

from pyspark.mllib.evaluation import BinaryClassificationMetrics
import StringIO
import gzip
import time
import zipfile
import io
import pickle


if sys.getdefaultencoding() != 'utf-8': 
    reload(sys) 
    sys.setdefaultencoding('utf-8')

#集群环境配置
conf = SparkConf().setMaster("spark://172.16.7.46:7077").setAppName('PE_test')\
    .set("spark.executor.memory", "3500m")\
    .set("spark.driver.maxResultSize", "2g")\
    .set('spark.worker.ui.retainedExecutors',"200")\
    .set('spark.worker.ui.retainedDrivers',"200")\
    .set('spark.network.timeout',"3600")\
    .set('spark.reducer.maxSizeInFlight',"100m")\
    .set('spark.shuffle.io.numConnectionsPerPeer',"2")\
    .set('spark.ui.retainedJobs',"200")\
    .set('spark.ui.retainedStages',"200")\
    .set('spark.executor.heartbeatInterval',"3600")\
    .set("spark.memory.offHeap.size","300m")\
    .set('spark.executor.cores',"2") \
    .set('spark.default.parallelism',"28")\
    .set('spark.driver.port',"43300")\
	.set('saprk.executor.port',"44444")\
    .set('spark.memory.fraction',"0.8")

sc = SparkContext(conf=conf)
sc.addPyFile('cs_byte_ng.py')
sc.addPyFile('ML.py')
from ML import RF_model_s
from ML import lrm_bfgs
from cs_byte_ng import *
try:
    import pefile
    print('import successfully')
except:
    print('import error')

#conf = sc._jsc.hadoopConfiguration()
#hconf.setBoolean("fs.hdfs.impl.disable.cache",True)
def read_fun_generator(filepath,gb):
    if ('MZ' in gb[:2]):  #PE文件
        return gb
    else:
        try:
            if filepath.endswith('.gz'):
                ac = StringIO.StringIO(gb)  # 压缩文件
                return gzip.GzipFile(fileobj = ac).read()
            elif filepath.endswith('.zip'):
                ac = io.BytesIO(gb)  # 压缩文件
                zobj = zipfile.ZipFile(file = ac , mode = 'r',compression=zipfile.ZIP_DEFLATED)
                data=[]
                teee = False
                for name in zobj.namelist():
                    if name.endswith('.exe') or name.endswith('.EXE'):
                        data = zobj.read(name)
                        teee = True
                        break
                #if len(data) < 1:
                 #   if teee:
                  #      print('read**error file',filepath)
                 #   else:
                 #       print(zobj.namelist())
                 #       print('no exe**error file', filepath)
                return data
            else:
                #print('not zipfile**error file', filepath)
                return []
        except:
            #print('Exception**error file', filepath)
            return []

def feature_transform(content,verbose =False): #content为二进制文件流
    from FeaExtract import feature_gets
    result= []
    if('MZ' in content[:2]):
        try:
            f =pefile.PE(data=content)
            result.append(feature_gets(f,'test',True))
            f.close()
            if verbose:
                print('one')

            #MoveMalwareFile(filepath,PESaveFileRoot) #移动文件
            #CopyMalwareFile(filepath,PESaveFileRoot)  #复制文件
        except Exception:
            #print(len(content))
            print('error')
            pass
    return  result
	
def ng_byte_feature_get(content):
    result= []
    if('MZ' in content[:2]):
        try:
            result = ng.gen_df(pefile.PE(data = content))
            #MoveMalwareFile(filepath,PESaveFileRoot) #移动文件
            #CopyMalwareFile(filepath,PESaveFileRoot)  #复制文件
        except Exception:
            print(len(content))
            #print('error')
            pass
    return  result

def filterFunc(feat):
    if isinstance(feat,list):
        return False
    return True

def read_fun_generator_b(ac):
    feature = gen_df(ac)
    #feature = ng_byte_feature_get(ac)
   # print('one')
    if len(feature) < 1:
        return []
    else:
        return LabeledPoint(0.0,feature)    #double,not int
    return []

def read_fun_generator_m(ac):
    feature = gen_df(ac)
    #feature = ng_byte_feature_get(ac)
    if len(feature) < 1:
        return []
    else:
        return LabeledPoint(1.0,feature)
    return []

def calcu_2g(content):
    # check the section excutable
    one_list = []
    N = 2
    tree = dict()
    try:
        pe = pefile.PE(data=content)
        for sect in pe.sections:
            if check_conditon(sect):
                one_list.extend(sect.get_data())
        lenlen = len(one_list)
        # print('section len is ******************************', lenlen)
        if lenlen > N and lenlen < 5463168:
            for i in range(lenlen - N + 1):
                if (one_list[i], one_list[i + 1]) not in tree:
                    tree[(one_list[i], one_list[i + 1])] = 1
    except Exception as e:
        pass
    return tree

def gram_one_file(content,verbose = False):
    #check the section excutable
    one_list = []
    N = 3
    tree = dict()
    g_3g_dict = broadcastVar.value
    try:
        pe = pefile.PE(data=content)
        for sect in pe.sections:
            if check_conditon(sect):
                if verbose:
                    print('the section name is %s' % sect.Name)
                one_list.extend(sect.get_data())
        lenlen = len(one_list)
        #print('section len is ******************************',lenlen)
        if lenlen > N and lenlen < 5463168:
			for i in range(lenlen - N + 1):
				a=one_list[i]
				b=one_list[i+1]
				c=one_list[i+2]
				if (a,b) in g_3g_dict:
					if (a,b,c) not in tree:
						tree[(a,b,c)] = 1
    except Exception as e:
        print('error infomation',e)
        pass
    print('the tree len is ',len(tree))
    return tree

def gen_df(content):
    binary_features = []
    features_all = broadcastVar.value
    if len(features_all)< 1:
        print('*********************************error****************************************')
        return binary_features
    try:
        N = 3
        order = 0
        gainFeatsPerClass = 2000
        one_list = []
        pe = pefile.PE(data=content)
        for sect in pe.sections:
            if check_conditon(sect):
                one_list.extend(sect.get_data())
        lenlen = len(one_list)
        binary_features.extend([0 for i in range(gainFeatsPerClass)])
        for i in range(lenlen - N + 1):
            strs = (one_list[i],one_list[i+1],one_list[i+2])
            if strs in features_all:
                binary_features[features_all[strs]] = 1
                order += 1
    except Exception:
        pass

    '''
    ## instead of binary features, do count
    grams_dict = dict()
    for gram in grams_string:
        if gram not in grams_dict:
            grams_dict[gram] = 1
        else:
            grams_dict[gram] += 1 

    binary_features = []
    for feature in features_all:
        if feature in grams_dict:
            binary_features.append(grams_dict[feature])
        else:
            binary_features.append(0)
    del grams_string   	
    '''
    return binary_features

def dict_exist(gdict):
    for k in gdict:
        print('**',k,gdict[k])
        break
	if len(gdict) > 0:
		return True
        print('dict exit ***************************',len(gdict))
	return False

#主函数
malRoot = 'hdfs://172.16.7.46:9000/dataset/bd-All-Series/home/zhuoxiong/2017-*/samples/*/'
benRoot = 'hdfs://172.16.7.46:9000/dataset/bd-All-Series/home/zhuoxiong/file_exe/*'
#benRoot2 = '/home/deyuan/Projects/Machine-Learning-Based-Malware-Detection-Engine/Industry/MLEngine/MalwarePEDetection/DataSet/benign' 

start_time = time.time()

Training = True
if Training:
    rdd_b = sc.binaryFiles(benRoot).map(lambda x:read_fun_generator(x[0],x[1]))
    rdd_m = sc.binaryFiles(malRoot).map(lambda x:read_fun_generator(x[0],x[1]))
    print('trainning start......')
    rddsb = rdd_b.randomSplit([2.0,2.0,2.0,2.0,2.0]) #根据实际数据配置
    rddsm = rdd_m.randomSplit([2.5, 7.5])
    tempRDD = rddsb[0].union(rddsb[2]).union(rddsb[4])
    N = 29401
    tempRDDm = rddsm[0]
    P = 30581
    print('trainset: benign: %d   malware:%d'%(N,P))

    #calculate 2g for 3g
   #print('all is ',tempRDD.count())
   #print('ball is ',tempRDD.map(calcu_2g).count)
    b2dict = tempRDD.map(calcu_2g).reduce(dict_add)
    pickle.dump(b2dict,open('cs_b2g.pl', 'wb'))
    m2dict = tempRDDm.map(calcu_2g).reduce(dict_add)
    pickle.dump(m2dict, open('cs_m2g.pl', 'wb'))
    print('the 2g dict information:',len(b2dict),len(m2dict))
    adict = dict_compose(b2dict, m2dict)
    del b2dict,m2dict
    cut2g_for_3g(adict)
    del adict
    print('calculate 2g is successful')

    g_3g_dict = pickle.load(open('cs_2g_for_3g.pl', 'rb'))
    broadcastVar = sc.broadcast(g_3g_dict)

    #calculate 3gram(training)
    bdictall = tempRDD.map(gram_one_file).reduce(dict_add)
    print('allaaaaaaaaaaaaaaaaaaaaaaaaaaa', len(bdictall))
    pickle.dump(bdictall, open('cs_b3g.pl', 'wb'))

    mdictall = tempRDDm.map(gram_one_file).reduce(dict_add)
    print('alllllllllllllllllllllll', len(mdictall))
    pickle.dump(mdictall, open('cs_m3g.pl', 'wb'))
	
    gdictall = dict_compose(mdictall, bdictall)
    del mdictall,bdictall
    dict_all = readTrainToEnd(gdictall, P, N)
    del gdictall
    getGainFeature(dict_all, P, N)
    print('training time is :',time.time() - start_time)
    sc.stop()
    sys.exit()
	

if not os.path.exists('cs_ngram_dict.pl'):
    exit('training Based is undefined')
features_all = pickle.load(open('cs_ngram_dict.pl','rb'))
broadcastVar = sc.broadcast(features_all)

rdd_b = sc.binaryFiles(benRoot).map(lambda x:read_fun_generator(x[0],x[1]))
rdd_m = sc.binaryFiles(malRoot).map(lambda x:read_fun_generator(x[0],x[1]))

rdd1_t =rdd_b.map(read_fun_generator_b).filter(filterFunc)  #spark method
rdd2_t = rdd_m.map(read_fun_generator_m).filter(filterFunc)  #spark method

#print('benign file is ',rdd1_t.count())
#print('malware file is ',rdd2_t.count())

rdds1 = rdd1_t.randomSplit([6.0,2.0,2.0]) #根据实际数据配置
rdds2 = rdd2_t.randomSplit([2.5, 2.0, 6.0])
#print('benign file is train:%d   cross:%d	test:%d'%(rdds1[0].count(),rdds1[1].count(),rdds1[2].count()))
#print('malware file is train:%d  cross:%d	test:%d'%(rdds2[0].count(),rdds2[1].count(),rdds2[2].count()))

#调参
lsr_pram=[[10],[15],[20],[25],[30]] 
rf_pram = ([200,7,32],[250,7,32],[300,7,32],[200,10,32],[200,15,32],[200,20,32]) 

best_rate = 0
best_param = None

trainrdds = rdds1[0].union(rdds2[0]) #训练集
trainCount = trainrdds.count()

#交叉验证
crossrdds = rdds1[1].union(rdds2[1]) 
crossCount = crossrddsrdds.count()
for i in range(len(lsr_pram)):
	#mlmodel = RF_model_s(trainrdds)
	ml = lrm_bfgs(trainrdds,lsr_pram[i][0])
	
	#非Tree的方法
	predict_labels = crossrdds.map(lambda p: (ml.predict(p.features),p.label))
	
	#Tree的方法，mllib的坑
	#presult = mlmodel.predict(crossrdds.map(lambda x: x.features))
	#predict_labels = presult.zip(crossrdds.map(lambda lp: lp.label)) 

	acc = 1.0 * predict_labels.filter(lambda x: x[0] == x[1]).count() / crossCount
	if acc > best_rate:
		best_rate = acc
		best_rate= lsr_pram[i]
print('the cross accuracy rate is ',best_rate)
print('the best parameter is ',best_param)

#以最优参数测试
#mlmodel = RF_model_s(trainrdds)
mlmodel = lrm_bfgs(trainrdds,best_rate[0])
#print(mlmodel.toDebugString())
testrdds = rdds1[2].union(rdds2[2])
testCount = testrdds.count()
print('trainning completely warning information')

#非Tree的方法
predictionAndLabels = testrdds.map(lambda p: (mlmodel.predict(p.features),p.label))

#Tree的方法，mllib的坑
#predictions = mlmodel.predict(testrdds.map(lambda x: x.features))
#predictionAndLabels = predictions.zip(testrdds.map(lambda lp: lp.label))

print('result analysis......................................................')
#metrics =BinaryClassificationMetrics(predictionAndLabels)
accuracy = 1.0 * predictionAndLabels.filter(lambda x: x[0] == x[1]).count() / testCount	


#经验误差
trainPL = trainrdds.map(lambda p: (mlmodel.predict(p.features),p.label))
trainAcc = 1.0 * trainPL.filter(lambda x: x[0] == x[1]).count() / trainCount	
print('training Error:',trainAcc)
	
#accuracy = metrics.accuracy
print('***********************************')
print('train num:',trainCount)
print('test_num:',testCount)
print('class model:LR')
print('the over all accuracy of the model is ',accuracy)
#print(metrics.confusionMatrix().toArray())
#print('the recall of malware',metrics.recall(1))
#print('the precision of malware',metrics.precision(1))
#print('the fmeasure of malware',metrics.fMeasure())
#print('malware false positive',metrics.falsePositiveRate(1))
print('the over all time is ',time.time() - start_time)
print('***********************************')
sc.stop()
sys.exit()

