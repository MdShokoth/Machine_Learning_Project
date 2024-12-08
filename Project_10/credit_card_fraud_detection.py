# -*- coding: utf-8 -*-
"""Credit_Card_Fraud_Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19knMwpozVbjZSAvMGmuFq6FAkBTpKbAC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df=pd.read_csv('/content/creditcard.csv')

df.head()

df.tail()

df.shape

df.info()

df.isnull().sum()

df.describe()

df.groupby('Class').mean()

df['Class'].value_counts()

"""Indicating large discrepancy. Bad for model. Let's split them into equal size"""

temp_zero=df[df.Class==0]
temp_one=df[df.Class==1]

temp_zero.shape

temp_one.shape

modified_temp_zero=temp_zero.sample(n=492)

df=pd.concat([modified_temp_zero,temp_one],axis=0)

df.Class.value_counts()

df.groupby('Class').mean()

X=df.drop(columns='Class',axis=1)
Y=df['Class']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,random_state=2)

model=LogisticRegression()

model.fit(X_train,Y_train)

Y_train_predict=model.predict(X_train)

print("Accuracy score",accuracy_score(Y_train,Y_train_predict))

X_train_predict=model.predict(X_test)

print("Accuracy score",accuracy_score(Y_test,X_train_predict))

