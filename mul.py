# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:24:54 2022

@author: SPTINT-05
"""

import pandas  as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
data=pd.read_csv('C:/Users/SPTINT-05/Downloads/train.csv')
#g=sns.countplot(x='Sex',hue='Survived',data=data)
#g=sns.countplot(x='Embarked',hue='Survived',data=data)
def add_family(df):
    df['Family_Size']=df['SibSp'] + df['Parch'] + 1
    return df
data=add_family(data)
print(data.head(10))
#g=sns.countplot(x='Family_Size',hue='Survived',data=data)
#g=sns.catplot(x='Embarked',hue='Sex',col='Survived',data=data,kind="count",height=4,aspect=.7)
g=sns.catplot(x='Embarked',hue='Sex',col='Survived',data=data,kind="count",height=4,aspect=.7)
