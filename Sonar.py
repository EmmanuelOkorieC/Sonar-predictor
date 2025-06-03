# Importing dependencies
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
import pickle

#loading the dataset
sonar_data = pd.read_csv('sonar data.csv', header = None)

#study data
print(sonar_data.head())
print(sonar_data.shape)
print(sonar_data.describe())
print(sonar_data[60].value_counts())
print(sonar_data.groupby(60).mean())
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

input = (0.1083,0.1070,0.0257,0.0837,0.0748,0.1125,0.3322,0.4590,0.5526,0.5966,0.5304,0.2251,0.2402,0.2689,0.6646,0.6632,0.1674,0.0837,0.4331,0.8718,0.7992,0.3712,0.1703,0.1611,0.2086,0.2847,0.2211,0.6134,0.5807,0.6925,0.3825,0.4303,0.7791,0.8703,1.0000,0.9212,0.9386,0.9303,0.7314,0.4791,0.2087,0.2016,0.1669,0.2872,0.4374,0.3097,0.1578,0.0553,0.0334,0.0209,0.0172,0.0180,0.0110,0.0234,0.0276,0.0032,0.0084,0.0122,0.0082,0.0143)
input_as_numpy_array = np.asarray(input)
input_reshaped = input_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_reshaped)
print(prediction)

if (prediction[0] == "R"):
 print("This object is a rock")
else:
 print("This Object is mine")


st.title("🔍 Sonar Rock or Mine Predictor")

input_text = st.text_area("Enter 60 comma-separated values below:", "")

if st.button("Predict"):
    try:
        input_list = [float(x) for x in input_text.strip().split(',')]
        if len(input_list) != 60:
            st.error("❌ Please enter exactly 60 numbers.")
        else:
            input_array = np.array(input_list).reshape(1, -1)
            prediction = model.predict(input_array)
            result = "🪨 Rock" if prediction[0] == "R" else "💣 Mine"
            st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"❌ Invalid input: {e}")

        