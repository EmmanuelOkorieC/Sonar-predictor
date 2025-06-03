# Importing dependencies
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

#loading the dataset
sonar_data = pd.read_csv('sonar data.csv', header = None)

#study data
#print(sonar_data.head())
#print(sonar_data.shape)
#print(sonar_data.describe())
#print(sonar_data[60].value_counts())
#print(sonar_data.groupby(60).mean())

#splitting data
X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)
print(X.shape, X_train.shape, X_test.shape)


#Model training
model = LogisticRegression()
model.fit(X_train, Y_train)

#training model evaluation
training_model_prediction =model.predict(X_train)
training_accuracy = accuracy_score(training_model_prediction, Y_train)
print(training_accuracy)

#test evaluation
test_model_prediction =model.predict(X_test)
test_accuracy = accuracy_score(test_model_prediction, Y_test)
print(test_accuracy)

#save model
pickle.dump(model, open("model.pkl", "wb"))

