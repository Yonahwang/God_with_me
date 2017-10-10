# -*- coding: utf-8 -*-
# !/usr/bin/python

# 导入需要用到的库
#form __futurn __ import division
import os
import random
from sklearn import metrics


from featureEX import *
import multiprocessing

# 全局参数配置，根据需要自己修改以下六个参数
Benign_File_Root = r"/Users/fengjiaowang/Downloads/small_data/normalpdf" # 正常样本数据集的文件路径
Melicious_File_Root = r"/Users/fengjiaowang/Downloads/small_data/malpdf" # 恶意样本数据集的文件路径

Benign_File_For_Trainning =10  # 用于训练的正常样本的个数
Melicious_File_For_Trainning =10  # 用于训练的恶意样本的个数
Benign_File_For_Test =10  # 用于测试的正常样本的个数
Melicious_File_For_Test =10  # 用于测试的恶意样本的个数


# Random Forest Classifier
def random_forest_classifier(train_x, train_y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=200)  # 根据自己的需要，指定随机森林的树的个数
    model.fit(train_x, train_y)
    return model


# 载入数据集
def load_file(PEfile_Path):
    test_files = list()
    for dirpath, dirname, filenames in os.walk(PEfile_Path):
        for filename in filenames:
            rfpath = os.path.join(dirpath, filename)
            test_files.append(rfpath)
    return test_files


# 数据采集随机化，避免过拟合
def datebase_divide(*arg):
    import math
    if len(arg) == 2:
        DatabaseTrainNum_Normal = int(math.floor(arg[0] / 2))
        DatabaseTestNum_normal = arg[0] - DatabaseTrainNum_Normal
        DatabaseTrainNum_Melidious = int(math.floor(arg[1] / 2))
        DatabaseTestNum_Melidious = arg[1] - DatabaseTrainNum_Normal
    else:
        DatabaseTrainNum_Normal = arg[0]
        DatabaseTestNum_normal = arg[1]
        DatabaseTrainNum_Melidious = arg[2]
        DatabaseTestNum_Melidious = arg[3]
    templist = [i for i in range(DatabaseTrainNum_Normal + DatabaseTestNum_normal)]
    trainlist_normal = random.sample(templist, DatabaseTrainNum_Normal)  # 选择正常的训练样本
    testlist_normal = [i for i in templist if i not in trainlist_normal]

    templist = [i + DatabaseTrainNum_Normal + DatabaseTestNum_normal for i in
                range(DatabaseTrainNum_Melidious + DatabaseTestNum_Melidious)]
    trainlist_melicious = random.sample(templist, DatabaseTrainNum_Melidious)
    testlist_melicious = [i for i in templist if i not in trainlist_melicious]

    trainlist = trainlist_normal + trainlist_melicious
    random.shuffle(trainlist)  # 训练样本随机性

    testlist = testlist_normal + testlist_melicious
    return trainlist, testlist



# 数据处理与特征提取，，此处需重点修改
def data_get(gcroot_normal, gcroot_melicious, trainSampleMark, testSampleMark, btotal):
    train_feature = []
    train_class = []
    test_feature = []
    test_class = []
    tename = []


    print("normal sample number is %d" % len(gcroot_normal))
    print("malware sample number is %d" % len(gcroot_melicious))
    print('begin to read the dataset')


    for i in trainSampleMark:
        try:
            cla = 0
            if i<btotal:
                froot = gcroot_normal[i]
            else:
                froot=gcroot_melicious[i - btotal]
                cla = 1
            #*******************************************************************
            pdf = fakeFile_check(froot)
            if pdf:
                train_class.append(cla)
                train_feature.append(feature_extract(pdf)) #对输入文件进行特征提取

        except Exception:
            print('file %s feature extracting meet ERROR'%froot)
            continue

    for i in testSampleMark:
        try:
            cla = 0
            if i<btotal:
                froot = gcroot_normal[i]
            else:
                froot=gcroot_melicious[i - btotal]
                cla = 1

                 # *******************************************************************
            pdf = fakeFile_check(froot)
            if pdf:
                test_class.append(cla)
                test_feature.append(feature_extract(pdf)) #对输入文件进行特征提取

                tname = froot.split('/')[-1]
                tename.append(tname)
        except Exception:
            print('file %s feature extracting meet ERROR' % froot)
            continue

    return train_feature, train_class, test_feature, test_class,tename


# 对测试数据分类
def ml_predict(clf, test_x):
    print('******************** Test Data Info *********************')
    print('#testing data: %d, dimension: %d' % (len(test_x), len(test_x[0])))
    if clf:
        predictp = clf.predict_proba(test_x)
        predict = clf.predict(test_x)
        return predict, predictp


# 分析识别率
def predect_calcu(predict, test_y, binary_class=True):
    if binary_class:
        precision = metrics.precision_score(test_y, predict)
        recall = metrics.recall_score(test_y, predict)

        confusion = metrics.confusion_matrix(test_y, predict)
        TP = confusion[1, 1]
        TN = confusion[0, 0]
        FP = confusion[0, 1]
        FN = confusion[1, 0]

        print("TP:%d *** TN:%d *** FP:%d *** FN:%d " % (TP, TN, FP, FN))
        print('precision: %.2f%%, recall: %.2f%%' % (100 * precision, 100 * recall))
    accuracy = metrics.accuracy_score(test_y, predict)
    print('accuracy: %.2f%%' % (100 * accuracy))
    return accuracy, confusion

def tabledemo(name,test_y,predict):
    table = {'name': name, 'test':test_y , 'predint': predict}
    import pandas as pand
    frame = pand.DataFrame(table)
    return frame


def main():
    print('start processing')
    trainSampleMark, testSampleMark = datebase_divide(Benign_File_For_Trainning,
                                                      Benign_File_For_Test,
                                                      Melicious_File_For_Trainning,
                                                      Melicious_File_For_Test)

    bfiles = load_file(Benign_File_Root)  # 载入正常样本文件路径
    mfiles = load_file(Melicious_File_Root)  # 载入恶意文件路径
    DatabaseTotalNums_Normal = Benign_File_For_Trainning + Benign_File_For_Test  # 所有正常样本的个数


    train_x, train_y, test_x, test_y,tena = data_get(bfiles, mfiles, trainSampleMark, testSampleMark, DatabaseTotalNums_Normal)
    #print tena
    print('******************** Train Data Info *********************')
    print('#train data: %d, dimension: %d' % (len(train_x), len(train_x[0])))
    clf = random_forest_classifier(train_x, train_y)
    predict, predictp = ml_predict(clf, test_x)
    #print'predint : ',list(predict)
    predect_calcu(predict, test_y)
    #print'test_y : ',test_y
    print('******************** flie name analysis *********************')
    print tabledemo(tena,test_y,predict)
    print('DONE')

if __name__ == '__main__':
    main()

