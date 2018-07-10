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
from sklearn.metrics import roc_curve

# mal_tarin1 = pd.read_csv('/home/yonah/Downloads/mimicus-master/data/contagio-mal.csv')
# mal_tarin2 = pd.read_csv('/home/yonah/Downloads/mimicus-master/data/virustotal-mal.csv')
# ben_tarin1 = pd.read_csv('/home/yonah/Downloads/mimicus-master/data/contagio.csv')
# ben_tarin2 = pd.read_csv('/home/yonah/Downloads/mimicus-master/data/google-ben.csv')
# f_tarin = pd.read_csv('/home/yonah/God_with_me/2018Q1/MLmodel2/example/merge_con.csv') # 10K samples, balanced dataset
f_tarin = pd.read_csv('/home/yonah/data/God_with_me/2018Q2/data-set/merge_real8W.csv')
# f_tarin = pd.read_csv('/home/yonah/Data/data-set/merge_20w.csv')   #26w samples all
#f_tarin = pd.read_csv('/home/yonah/God_with_me/2018Q2/MLmodel3/example/test4K.csv')


def data_clear(file):
    # label = file[['class']]

    '''a = file['class']=='FALSE'
    b = file['class'] == 'TRUE'
    file.loc[a,'class'] = False
    file.loc[b, 'class'] = True'''

    file['class'] = file['class'].astype(bool)
    file['class'] = file['class'].astype(int)
    y = file[['class', 'filename']]
    NY = np.array(y)
    NYY = NY.tolist()

    # print y
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

    return NYY, Xint.tolist(), feat_id


# 对测试数据分类
def ml_predict(clf, test_x):
    print('******************** Test Data Info *********************')
    print('#testing data: %d, dimension: %d' % (len(test_x), len(test_x[0])))
    if clf:
        predictp = clf.predict_proba(test_x)
        predict = clf.predict(test_x)
        return predict, predictp


# Random Forest Classifier
def random_forest_classifier(train_x, train_y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, oob_score=False)  # 根据自己的需要，指定随机森林的树的个数
    model.fit(train_x, train_y)
    return model


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


def plot_feature_importance(feat, imp):
    dic = {'feat': feat, 'imp': imp}
    data = DataFrame(dic)
    data.to_csv("feature_importance.csv", index=False, sep=',')
    newI = data.sort_values(by='imp', axis=0, ascending=False)
    newI.index = [i for i in range(len(newI))]
    x_str = newI['feat'].tolist()
    y = newI['imp'].tolist()

    plt.barh(range(len(x_str[0:30])), y[0:30], color='g', tick_label=x_str[0:30])
    ax = plt.gca()
    plt.subplots_adjust(left=0.2, bottom=0.1, right=0.9, top=0.8, hspace=0.2, wspace=0.3)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45)
    plt.savefig('importance.jpg')
    plt.show()


def table_feature_importance(feat, imp):
    df = pd.DataFrame(columns=['feature', 'importance'])
    df['feature'] = feat
    df['importance'] = imp
    df.to_csv('impportance_featuer.csv', index=False, sep=',')


def AnalysisTofile(name1, test1, predict1, prob):
    name = []
    test = []
    predict = []
    proba = []
    for i in range(len(predict1)):
        name.append(name1[i])
        test.append(test1[i])
        predict.append(predict1[i])
        proba.append(prob[i])
    df = DataFrame(columns=('name', 'leble', 'RF', 'Proba'))  # 生成空的pandas表
    df['name'] = name
    df['leble'] = test
    df['RF'] = predict
    df['Proba'] = proba
    df['diff'] = df['RF'] - df['leble']
    # print newdf.head(10)
    return df[df['diff'] != 0]


def ySpilt(list):
    DF_y = pd.DataFrame(list, columns=['Y', 'finame'])
    DF = DF_y['Y']
    DF2 = DF_y['finame']
    y = DF.tolist()
    finame = DF2.tolist()
    return y, finame



def main():
    print('start processing')
    y, X, f_id = data_clear(f_tarin)
    from sklearn.model_selection import train_test_split
    train_x, test_x, train_Y, test_Y = train_test_split(X, y, random_state=5)  # randomize samples
    train_y, _ = ySpilt(train_Y)
    test_y, fina = ySpilt(test_Y)

    print('******************** RF Train Data Info *********************')
    print('#train data: %d, dimension: %d' % (len(train_x), len(train_x[0])))
    clf = random_forest_classifier(train_x, train_y)
    # plot_feature_importance(f_id,clf.feature_importances_)   #draw importance plot
    table_feature_importance(f_id, clf.feature_importances_)
    predict, predictp = ml_predict(clf, test_x)  # test
    predect_calcu(predict, test_y)


    print('******************** flie analysis *********************')
    proba = clf.predict_proba(test_x)
    print AnalysisTofile(fina, test_y, predict, proba)
    end = datetime.datetime.now()
    print "spend time detction = %d s" % (end - start).seconds
    '''with open('model_csv3.1.pickle', 'wb') as f:   # 保存模型
        pickle.dump(clf, f)'''
    print('DONE')


if __name__ == '__main__':
    start = datetime.datetime.now()
    main()

    end = datetime.datetime.now()
    print "spend time = %d s" % (end - start).seconds




