#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
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



#f_tarin = pd.read_csv('/home/yonah/God_with_me/2018Q2/MLmodel3/example/merge_real.csv') # 10K samples, balanced dataset
f_tarin = pd.read_csv('/home/yonah/God_with_me/2018Q2/MLmodel3/example/test4K.csv')

def data_clear(file,num):

    #a = file['class']=='FALSE'
    #b = file['class'] == 'TRUE'
    #file.loc[a,'class'] = False
    #file.loc[b, 'class'] = True

    file['class'] = file['class'].astype(bool)
    file['class'] = file['class'].astype(int)
    #print file['class']
    #  print file.loc[file['class']==0]   #  print x ==0 lines
    y = file[['class','filename']]
    NY = np.array(y)
    NYY = NY.tolist()
    feature = ['count_acroform_obs', 'count_box_legal', 'count_box_overlap', 'count_image_xlarge', 'count_objstm_obs',
     'createdate_dot', 'keywords_dot', 'moddate_dot', 'pdfid0_dot', 'pdfid1_dot', 'pos_acroform_avg',
     'pos_acroform_max', 'pos_acroform_min', 'pos_box_avg', 'pos_box_max', 'pos_box_min', 'pos_eof_avg', 'pos_eof_max',
     'pos_eof_min', 'pos_image_avg', 'pos_image_max', 'pos_image_min', 'pos_page_avg', 'pos_page_max', 'pos_page_min',
     'ratio_size_obj', 'ratio_size_page', 'ratio_size_stream', 'count_image_xsmall', 'subject_num', 'count_js_obs',
     'keywords_num', 'company_mismatch', 'count_action_obs', 'count_font_obs', 'count_image_med', 'subject_dot',
     'image_mismatch', 'count_box_a4', 'count_page_obs', 'count_javascript_obs', 'keywords_mismatch', 'keywords_uc',
     'subject_uc', 'subject_mismatch', 'pdfid1_lc', 'ratio_imagepx_size', 'author_dot', 'keywords_oth',
     'count_image_small', 'pdfid0_lc', 'keywords_lc', 'count_image_large', 'author_num', 'pdfid1_oth', 'keywords_len',
     'title_mismatch', 'author_mismatch', 'creator_mismatch', 'count_image_total', 'count_stream_diff', 'pdfid0_oth',
     'author_oth', 'author_lc', 'creator_num', 'count_objstm', 'delta_tz', 'creator_dot', 'image_totalpx', 'author_uc',
     'count_acroform', 'delta_ts', 'pdfid0_uc', 'createdate_ts', 'count_action', 'subject_oth', 'count_xref',
     'author_len', 'creator_oth', 'box_nonother_types', 'moddate_ts', 'title_lc', 'version', 'title_uc', 'subject_len',
     'title_dot', 'createdate_tz', 'pdfid1_uc', 'count_trailer', 'title_len', 'len_stream_min', 'title_num',
     'subject_lc', 'count_eof', 'moddate_tz', 'createdate_mismatch', 'count_box_letter', 'moddate_mismatch',
     'pdfid_mismatch', 'creator_uc', 'box_other_only', 'creator_lc', 'title_oth', 'moddate_version_ratio',
     'creator_len', 'createdate_version_ratio', 'pdfid0_mismatch', 'pdfid1_mismatch', 'count_page', 'len_obj_min',
     'count_startxref', 'producer_num', 'len_stream_max', 'pdfid1_len', 'producer_uc', 'pdfid0_num', 'len_obj_avg',
     'len_stream_avg', 'len_obj_max', 'producer_mismatch', 'producer_lc', 'pdfid0_len', 'count_js', 'count_endstream',
     'count_stream', 'count_box_other', 'producer_dot', 'pdfid1_num', 'producer_len', 'producer_oth', 'count_endobj',
     'count_obj', 'size', 'count_javascript', 'count_font']

    '''feature= ['author_dot', 'author_lc', 'author_len', 'author_mismatch', 'author_num', 'author_oth', 'author_uc',
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
                'title_mismatch', 'title_num', 'title_oth', 'title_uc', 'version']'''

    X = file[feature[:num]]
    feat_id = X.columns.tolist()

    XX = np.array(X)
    Xint = XX.astype(int)
    return NYY,Xint.tolist()


def SVM(X_train,y_train,X_test,data_y):
    from sklearn.svm import SVC
    model = SVC(C=1.0)
    # 拟合模型
    model.fit(X_train, y_train)
    # 模型预测
    return model.predict(X_test), model.score(X_test, data_y)

def NNet(X_train,y_train,X_test,data_y):
    from sklearn.neural_network import MLPClassifier
    model = MLPClassifier(activation='relu', solver='adam', alpha=0.0001)
    # 拟合模型
    model.fit(X_train, y_train)
    # 模型预测
    return model.predict(X_test), model.score(X_test, data_y)

def KNN(X_train,y_train,X_test,data_y):
    from sklearn import neighbors
    model = neighbors.KNeighborsClassifier(n_neighbors=5, n_jobs=1)  # 分类
    #model = neighbors.KNeighborsRegressor(n_neighbors=5, n_jobs=1)  # 回归
    # 拟合模型
    model.fit(X_train, y_train)
    # 模型预测
    return model.predict(X_test), model.score(X_test, data_y)

def NB(X_train,y_train,X_test,data_y):
    from sklearn import naive_bayes
    #model = naive_bayes.GaussianNB()  # 高斯贝叶斯
    model = naive_bayes.MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)
    #model = naive_bayes.BernoulliNB(alpha=1.0, binarize=0.0, fit_prior=True, class_prior=None)
    # 拟合模型
    model.fit(X_train, y_train)
    # 模型预测
    return model.predict(X_test), model.score(X_test, data_y)

def RF(X_train,y_train,X_test,data_y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=200)  # 根据自己的需要，指定随机森林的树的个数
    model.fit(X_train, y_train)
    # 拟合模型
    model.fit(X_train, y_train)
    # 模型预测
    impf = model.feature_importances_
    print impf
    return model.predict(X_test), model.score(X_test, data_y)




def ySpilt(list):
    DF_y = pd.DataFrame(list, columns=['Y', 'finame'])
    DF = DF_y['Y']
    DF2 = DF_y['finame']
    y = DF.tolist()
    finame = DF2.tolist()
    return y,finame


def classif(X,y):
    print('start processing')

    from sklearn.model_selection import train_test_split
    train_x, test_x, train_Y, test_Y = train_test_split(X, y, test_size=0.2, random_state=1,)  # randomize samples
    train_y, _ = ySpilt(train_Y)
    test_y,fina = ySpilt(test_Y)

    print('********************Train Data Info *********************')
    print('#train data: %d, dimension: %d' % (len(train_x), len(train_x[0])))
    FileOne1, ac1 = RF(train_x, train_y,test_x,test_y)
    #FileOne2, ac2 = NB(train_x, train_y, test_x, test_y)
    FileOne3, ac3 = KNN(train_x, train_y, test_x, test_y)
    FileOne4, ac4 = NNet(train_x, train_y, test_x, test_y)
    FileOne5, ac5 = SVM (train_x, train_y, test_x, test_y)
    ac1_list.append(ac1)
    ac3_list.append(ac3)
    ac4_list.append(ac4)
    ac5_list.append(ac5)

    #print('******************** flie analysis *********************')
    #print AnalysisTofile(tena, test_y, predict)
    end = datetime.datetime.now()
    print "spend time detction = %d s" % (end - start).seconds
    print('DONE')


def fact(n):
    if n==0:
        return 1
    y, featu = data_clear(f_tarin,n)
    classif(featu,y)
    return n * fact(n - 1)

if __name__ == '__main__':
    start = datetime.datetime.now()
    ac1_list = []
    ac3_list = []
    ac4_list = []
    ac5_list = []
    #fact(135)
    y, featu = data_clear(f_tarin,135)
    classif(featu, y)
    dataframe = pd.DataFrame({'RF': ac1_list, 'KNN': ac3_list, 'NNET': ac4_list, 'SVM': ac5_list})
    print dataframe
    #dataframe.to_csv("Robustnes.csv", index=False, sep=',')

    end = datetime.datetime.now()
    print "spend time = %d s" % (end - start).seconds