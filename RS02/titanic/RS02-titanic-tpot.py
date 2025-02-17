# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Content：对Titanic数据进行清洗，建模并对乘客生存进行预测。使用TPOT
# Author:  HuiHui
# Date:    2020-03-12
# Reference:

import numpy as np
import pandas as pd
from tpot import TPOTClassifier #自动机器学习
from sklearn.model_selection import cross_val_score #交叉验证
from sklearn.feature_extraction import DictVectorizer

#数据加载
train_data = pd.read_csv('./train.csv') # 返回DataFrame类型
test_data = pd.read_csv('./test.csv')

# 数据探索
# 查看train_data信息
#pd.set_option('display.max_columns', None) #显示所有列

# print('查看数据信息：列名、非空个数、类型等')
# print(train_data.info())
# print(test_data.info())
# print('-'*30)
# print('查看数据摘要') #均值、方差等
# print(train_data.describe())
# print('-'*30)
# print('查看离散数据分布')
# print(train_data.describe(include=['O'])) #
# print('-'*30)
# print('查看前5条数据')
# print(train_data.head())

# 使用平均年龄来填充年龄中的nan值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
# 使用票价的均值填充票价中的nan值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)

print(train_data['Embarked'].value_counts()) #S最多
# 使用登录最多的港口来填充登录港口的nan值
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S',inplace=True)
# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]
print('特征值')
print(train_features)
# DictVectorizer对非数字化(Embarked、Sex)的特征采用0/1的方式进行量化，而数值型的特征一般情况维持原值即可
dvec=DictVectorizer(sparse=False)
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))
test_features=dvec.transform(test_features.to_dict(orient='record'))
print(dvec.feature_names_)

#TPOT生存预测
tpot = TPOTClassifier(generations=5, population_size=20, verbosity=2)
tpot.fit(train_features, train_labels)

# 得到TPOT准确率(基于训练集)
acc_decision_tpot = round(tpot.score(train_features, train_labels), 6) #round（）四舍五入
print(u'score准确率为 %.4lf' % acc_decision_tpot)

# 使用K折交叉验证统计TPOT准确率
print(u'cross_val_score准确率为 %.4lf' % np.mean(cross_val_score(tpot, train_features, train_labels, cv=10)))

tpot.export('tpot_titanic_pipeline.py')





