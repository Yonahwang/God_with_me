# -*- coding: utf-8 -*-
# !/usr/bin/python

# 第一步,提取特征
def extract_feature(file_path):
    # 提取一个文件的特征,返回值为 特征名字列表 和 数值列表
    return ['size','objects'],[10,8]

all_file_paths = [] # 需要提取特征的所有文件的路径
for file_path in all_file_paths:
    feature_names,feature_nums = extract_feature(file_path)

    # 将所有的特征转换为 "size_10" 这个形式
    features = []
    for i in len(feature_names):
        feature = feature_names + '_' + str(feature_nums)
        features.append(feature)

    # 标记是恶意还是良性
    features.append('mal_or_ben_'+str(1))

    # 将特征保存到文件
    # save(feature_path,features)

# 第二步,读取第一步保存的特征
features_set = set() # 所有特征
all_fea_paths = []
all_file_features = []
for fea_path in all_fea_paths:
    features = []
    
    # 打开特征文件,读取每一行
    f = open(fea_path)
    for line in f.readlines():
        str = line.split('_')
        feature_name = str[0]
        feature_num = int(str[1])
        
        # 更新特征集合
        features_set.update(feature_names)
        
        # 保存特征
        features.append({'name':feature_name,'num':feature_num})
    all_file_features.append(features)

# 第三步,转换为特征集

# 生成特征所属的下标
fea_index_dict = {}
for feature in features_set:
    fea_index_dict[feature] = len(fea_index_dict)

full_fea_list = []
for features in all_file_features:
    # 初始化所以特征为0
    fea_list = [0 for i in range(0, len(fea_index_dict))]
    for feature in features:
        fea_list[fea_index_dict[feature['name']]] = feature['num']
    
    # 保存
    full_fea_list.append(fea_list)

# full_fea_list 就是二维表了,全是数字,转换一下就可以使用到 机器学习中
# 下面使用pandas进行保存
import pandas as pd
column_list = features_set
df = pd.DataFrame(full_fea_list, columns=column_list)

# 将数据保存
df.to_csv('transfered.csv', index=False)

'''
# 下次读取
def get_features(self):
    self.__df = pd.read_csv('transfered.csv')

    y_data = self.__df['mal_or_ben']
    del self.__df['mal_or_ben']
    
    X_data = np.array(self.__df)

    print('get_features() finished')
    return X_data, y_data
'''

 
 