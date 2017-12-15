# -*- coding: utf-8 -*-
# !/usr/bin/python

# ��һ��,��ȡ����
def extract_feature(file_path):
    # ��ȡһ���ļ�������,����ֵΪ ���������б� �� ��ֵ�б�
    return ['size','objects'],[10,8]

all_file_paths = [] # ��Ҫ��ȡ�����������ļ���·��
for file_path in all_file_paths:
    feature_names,feature_nums = extract_feature(file_path)

    # �����е�����ת��Ϊ "size_10" �����ʽ
    features = []
    for i in len(feature_names):
        feature = feature_names + '_' + str(feature_nums)
        features.append(feature)

    # ����Ƕ��⻹������
    features.append('mal_or_ben_'+str(1))

    # ���������浽�ļ�
    # save(feature_path,features)

# �ڶ���,��ȡ��һ�����������
features_set = set() # ��������
all_fea_paths = []
all_file_features = []
for fea_path in all_fea_paths:
    features = []
    
    # �������ļ�,��ȡÿһ��
    f = open(fea_path)
    for line in f.readlines():
        str = line.split('_')
        feature_name = str[0]
        feature_num = int(str[1])
        
        # ������������
        features_set.update(feature_names)
        
        # ��������
        features.append({'name':feature_name,'num':feature_num})
    all_file_features.append(features)

# ������,ת��Ϊ������

# ���������������±�
fea_index_dict = {}
for feature in features_set:
    fea_index_dict[feature] = len(fea_index_dict)

full_fea_list = []
for features in all_file_features:
    # ��ʼ����������Ϊ0
    fea_list = [0 for i in range(0, len(fea_index_dict))]
    for feature in features:
        fea_list[fea_index_dict[feature['name']]] = feature['num']
    
    # ����
    full_fea_list.append(fea_list)

# full_fea_list ���Ƕ�ά����,ȫ������,ת��һ�¾Ϳ���ʹ�õ� ����ѧϰ��
# ����ʹ��pandas���б���
import pandas as pd
column_list = features_set
df = pd.DataFrame(full_fea_list, columns=column_list)

# �����ݱ���
df.to_csv('transfered.csv', index=False)

'''
# �´ζ�ȡ
def get_features(self):
    self.__df = pd.read_csv('transfered.csv')

    y_data = self.__df['mal_or_ben']
    del self.__df['mal_or_ben']
    
    X_data = np.array(self.__df)

    print('get_features() finished')
    return X_data, y_data
'''

 
 