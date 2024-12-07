# -*- coding: utf-8 -*-
"""Wine_Quality_Predict.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BgBn6aN6l0q_LvWbMm2xAZLLBNSxvwGb
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv("/content/winequality-red.csv")

df.head()

df.shape

df.describe()

df.isnull().sum()

sns.catplot(x="quality",data=df,kind="count")

sns.countplot(x='quality', data=df)

plt.figure(figsize=(5,5))
plt.bar(df['quality'],df['volatile acidity'])
plt.xlabel('quality')
plt.ylabel('volatile acidity')
plt.show()

plt.figure(figsize=(5,5))
sns.barplot(x='quality',y='citric acid',data=df)
plt.show()

correlation=df.corr()

sns.heatmap(correlation,cbar=True,square=True,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues')

X=df.drop('quality',axis=1)

Y=df['quality'].apply(lambda y:1 if y>=7 else 0)

print(Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)

classifier=RandomForestClassifier()
classifier.fit(X_train,Y_train)

predict_Y_train=classifier.predict(X_train)
training_data_accuracy=accuracy_score(predict_Y_train,Y_train)

print(training_data_accuracy)

predict_Y_test=classifier.predict(X_test)
testing_data_accuracy=accuracy_score(predict_Y_test,Y_test)

print(testing_data_accuracy)

sample_data=(8.5,0.28,0.56,1.8,0.092,35.0,103.0,0.9969,3.3,0.75,10.5)

sample_data=np.asarray(sample_data).reshape(1,-1)

if(classifier.predict(sample_data)==1):
  print("Good Quality Wine")
else:
  print("Bad Quality Wine")

