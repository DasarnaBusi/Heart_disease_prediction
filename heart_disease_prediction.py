# -*- coding: utf-8 -*-
"""Heart_disease_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ctwre-65KdFU8dICt_7BOOhZxXlkCDZn
"""

#Importing the libraries
import numpy as np
import pandas as pd
#Importing SkLearn libraries/modules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Importing the data
data = pd.read_csv("/content/heart_disease_data.csv")

data.head()

data.shape

data.info()

data.isnull().sum()

data.describe()

data['target'].value_counts()

#Splitting features and target
X = data.drop(columns = "target", axis = 1)
X

Y = data['target']
Y

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state=42)

X_train.shape

X_test.shape

Y_train.shape

Y_test.shape

model = LogisticRegression()

model.fit(X_train, Y_train)

#Evaluation of accuracy for training data
X_train_prediction = model.predict(X_train)
training_accuracy = accuracy_score(X_train_prediction, Y_train)
print(f"The training accuracy is {training_accuracy}")

#Evaluation of accuracy for testing data
X_test_prediction = model.predict(X_test)
testing_accuracy = accuracy_score(X_test_prediction, Y_test)
print(f"The testing accuracy is {testing_accuracy}")

#Prediction model
input_data = (54, 0, 2, 140, 290, 0, 0, 155, 1, 1.4, 1, 1, 3)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)
prediction = model.predict(input_data)
prediction
if prediction[0]=="0":
  print("Healthy person")
else:
  print("Heart Disease Found")
