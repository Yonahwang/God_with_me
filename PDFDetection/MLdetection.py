#!/usr/bin/python
# -*- coding: utf-8 -*-


# !/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import numpy as np
import pandas as pd
import datetime
from sklearn import datasets, linear_model
from sklearn import metrics
import pickle
import matplotlib.pyplot as plt
import random
from pandas import DataFrame
from sklearn.metrics import roc_curve

t_test = pd.read_csv('./testmal.csv')

def data_clear(file):
    #label = file[['class']]

    '''a = file['class']=='FALSE'
    b = file['class'] == 'TRUE'
    file.loc[a,'class'] = False
    file.loc[b, 'class'] = True'''


    file['class'] = file['class'].astype(bool)
    file['class'] = file['class'].astype(int)
    #print file['class']
    #  print file.loc[file['class']==0]   #  print x ==0 lines
    y = file[['class', 'filename']]
    NY = np.array(y)
    NYY = NY.tolist()


    #print y
    X = file[['author_dot', 'author_lc', 'author_len', 'author_mismatch', 'author_num', 'author_oth', 'author_uc',
                'box_nonother_types', 'box_other_only', 'company_mismatch', 'count_acroform', 'count_acroform_obs',
                'count_action', 'count_action_obs', 'count_box_a4', 'count_box_legal', 'count_box_letter',
                'count_box_other', 'count_box_overlap', 'count_endobj', 'count_endstream', 'count_eof', 'count_font',
                'count_font_obs', 'count_image_large', 'count_image_med', 'count_image_small', 'count_image_total',
                'count_image_xlarge', 'count_image_xsmall', 'count_javascript', 'count_javascript_obs', 'count_js',
                'count_js_obs', 'count_obj', 'count_objstm', 'count_objstm_obs', 'count_page', 'count_page_obs',
                'count_startxref', 'count_stream', 'count_stream_diff', 'count_trailer', 'count_xref', 'createdate_dot',
                'createdate_mismatch', 'createdate_ts', 'createdate_tz', 'createdate_version_ratio', 'creator_dot',
                'creator_lc', 'creator_len', 'creator_mismatch', 'creator_num', 'creator_oth', 'creator_uc', 'delta_ts',
                'delta_tz', 'image_mismatch', 'image_totalpx', 'keywords_dot', 'keywords_lc', 'keywords_len',
                'keywords_mismatch', 'keywords_num', 'keywords_oth', 'keywords_uc', 'len_obj_avg', 'len_obj_max',
                'len_obj_min', 'len_stream_avg', 'len_stream_max', 'len_stream_min', 'moddate_dot', 'moddate_mismatch',
                'moddate_ts', 'moddate_tz', 'moddate_version_ratio', 'pdfid0_dot', 'pdfid0_lc', 'pdfid0_len',
                'pdfid0_mismatch', 'pdfid0_num', 'pdfid0_oth', 'pdfid0_uc', 'pdfid1_dot', 'pdfid1_lc', 'pdfid1_len',
                'pdfid1_mismatch', 'pdfid1_num', 'pdfid1_oth', 'pdfid1_uc', 'pdfid_mismatch', 'pos_acroform_avg',
                'pos_acroform_max', 'pos_acroform_min', 'pos_box_avg', 'pos_box_max', 'pos_box_min', 'pos_eof_avg',
                'pos_eof_max', 'pos_eof_min', 'pos_image_avg', 'pos_image_max', 'pos_image_min', 'pos_page_avg',
                'pos_page_max', 'pos_page_min', 'producer_dot', 'producer_lc', 'producer_len', 'producer_mismatch',
                'producer_num', 'producer_oth', 'producer_uc', 'ratio_imagepx_size', 'ratio_size_obj',
                'ratio_size_page', 'ratio_size_stream', 'size', 'subject_dot', 'subject_lc', 'subject_len',
                'subject_mismatch', 'subject_num', 'subject_oth', 'subject_uc', 'title_dot', 'title_lc', 'title_len',
                'title_mismatch', 'title_num', 'title_oth', 'title_uc', 'version']]

    feat_id = X.columns.tolist()
    XX = np.array(X)
    Xint = XX.astype(int)

    return  NYY,Xint.tolist(),feat_id

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

# 对测试数据分类
def ml_predict(clf, test_x):
    print('******************** Test Data Info *********************')
    print('#testing data: %d, dimension: %d' % (len(test_x), len(test_x[0])))
    if clf:
        predictp = clf.predict_proba(test_x)
        predict = clf.predict(test_x)
        return predict, predictp

def ySpilt(list):
    DF_y = pd.DataFrame(list, columns=['Y', 'finame'])
    DF = DF_y['Y']
    DF2 = DF_y['finame']
    y = DF.tolist()
    finame = DF2.tolist()
    return y,finame

def AnalysisTofile(name1,test1,predict1):
    name = []
    test = []
    predict = []
    for i in range(len(predict1)):
        name.append(name1[i])
        test.append(test1[i])
        predict.append(predict1[i])
    df = DataFrame(columns=('name', 'leble', 'RF'))  # 生成空的pandas表
    df['name'] = name
    df['leble'] = test
    df['RF'] = predict

    df['diff'] = df['RF'] - df['leble']

    # print newdf.head(10)
    return df[df['diff'] != 0]

def main():
    y, X, f_id = data_clear(t_test)
    test_y, fina = ySpilt(y)

    #M = pickle.load('model_csv3.1.pickle','r')
    # 使用模型预测
    f2 = open('/home/yonah/God_with_me/2018Q2/MLmodel3/model_csv3.1.pickle', 'r')
    s2 = f2.read()
    clf = pickle.loads(s2)
    #clf2.predit(X, y)
    predict, predictp = ml_predict(clf, X)  # test
    #M.predit(X, test_y)

    print('******************** flie analysis *********************')
    print AnalysisTofile(fina, test_y, predict)
    predect_calcu(predict, test_y)

    end = datetime.datetime.now()
    print "spend time detction = %d s" % (end - start).seconds
    print('DONE')


if __name__ == '__main__':
    start = datetime.datetime.now()
    main()

    end = datetime.datetime.now()
    print "spend time = %d s" % (end - start).seconds



