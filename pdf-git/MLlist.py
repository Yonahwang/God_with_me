# -*- coding: utf-8 -*-
# !/usr/bin/python




from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import datetime
import random
from classfeature import *
from fileSelection import *



# Random Forest Classifier
def random_forest_classifier(train_x, train_y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=200)  # 根据自己的需要，指定随机森林的树的个数
    model.fit(train_x, train_y)
    return model

def plot_importance(f_v,fe_id):
    f_id = fe_id
    #f_id = [str(i) for i in range(len(f_v))]
    f_v = 100.0 * (f_v / f_v.max())

    f_id = np.array(f_id)

    sorted_idx = np.argsort(-f_v)

    pos = np.arange(len(sorted_idx)) + 0.5
    plt.subplot(1, 2, 2)
    plt.title('Feature Importance')

    plt.barh(pos[0:30], f_v[sorted_idx][0:30], color='r', align='center')
    plt.yticks(pos[0:30], f_id[sorted_idx][0:30])
    plt.xlabel('Relative Importance')
    plt.draw()
    plt.show()


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


def tabledemo(name1,test1,predict1):
    name = []
    test = []
    predict= []
    for i in range(len(predict1)):
        if test1[i] != predict1[i]:
            name.append(name1[i])
            test.append(test1[i])
            predict.append(predict1[i])
    table = {'name': name, 'test':test , 'predint': predict}
    import pandas
    frame = pandas.DataFrame(table)
    return frame


def main():


    print('******************** Train Data Info *********************')
    print('#train data: %d, dimension: %d' % (len(train_feature), len(train_feature[0])))
    clf = random_forest_classifier(train_feature, train_y)
    plot_importance(clf.feature_importances_, f_id)
    # RF_Information_print(clf)
    predict, predictp = ml_predict(clf, test_feature)
    # print'predint : ',list(predict)
    predect_calcu(predict, test_y)
    # print'test_y : ',test_y
    print('******************** flie analysis *********************')
    print tabledemo(tena, test_y, predict)
    print('DONE')



if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    print "spend time = %d s" % (end - start).seconds