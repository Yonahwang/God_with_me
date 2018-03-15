#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入需要用到的库
import os
import numpy as np
import datetime
from sklearn import metrics
import pickle


def main():
    print('start processing')
    global  nordict,maldict

    if True:
        if os.path.exists('normdictfile.pl'):
            nordict = pickle.load(open('normdictfile.pl','rb'))
        if os.path.exists('maldictfile.pl'):
            maldict = pickle.load(open('maldictfile.pl','rb'))



    trainSampleMark, testSampleMark = datebase_divide(Benign_File_For_Trainning,
                                                      Benign_File_For_Test,
                                                      Melicious_File_For_Trainning,
                                                      Melicious_File_For_Test)
    #train_x = train_feature ,train_y = train_class, test_x = test_feature
    train_x, train_y, test_x, test_y,tena,f_id= data_get(trainSampleMark, testSampleMark)
    print f_id
    print('normdict len is %d,maldict len is %d'%(len(maldict),len(nordict)))
    pickle.dump(nordict, open('normdictfile.pl', 'wb'))
    pickle.dump(maldict, open('maldictfile.pl', 'wb'))

    # make libsvm
    feature_x = train_x + test_x
    class_y = train_y + test_y
    from sklearn.datasets import dump_svmlight_file
    dump_svmlight_file(feature_x, class_y, 'libsvmby1.dat', zero_based=False, multilabel=False)
    start = datetime.datetime.now()
    print('******************** Train Data Info *********************')
    print('#train data: %d, dimension: %d' % (len(train_x), len(train_x[0])))
    clf = random_forest_classifier(train_x, train_y)
    plot_importance(clf.feature_importances_,f_id)
    #RF_Information_print(clf)
    predict, predictp = ml_predict(clf, test_x)
    #print'predint : ',list(predict)
    predect_calcu(predict, test_y)
    #print'test_y : ',test_y
    print('******************** flie analysis *********************')
    print tabledemo(tena,test_y,predict)
    end = datetime.datetime.now()
    print "spend time detction = %d s" % (end - start).seconds
    # 保存模型
    with open('model1.0.pickle', 'wb') as f:
        pickle.dump(clf, f)
    print('DONE')

if __name__ == '__main__':
    start = datetime.datetime.now()
    main()

    end = datetime.datetime.now()
    print "spend time = %d s" % (end - start).seconds