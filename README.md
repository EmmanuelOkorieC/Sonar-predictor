# Sonar Rock or Mine Predictor

This is a machine learning web app that predicts whether a sonar signal is from a **rock** or a **mine** based on 60 input features.

Built with:
- Python & Scikit-learn
- Streamlit for the user interface
- Logistic Regression for classification

## Try the Live App

[Click here to use the predictor](https://sonar-predictor-tpgx4wcyztl.streamlit.app/)

##  How It Works

1. Enter 60 comma-separated values from sonar data.
2. Click **Predict**.
3. The app tells you if the object is a **rock** or a **mine**.

## Files in this Repo

- `Sonar.py` – Main Streamlit app
- `model.pkl` – Trained logistic regression model
- `train_model.py` - Script to train the logistic regression model and save it as `model.pkl`
- 'sonar_data.csv' - Sonar Data used for training the Model. Available on [UCI ML Reository](https://archive.ics.uci.edu/ml/datasets/Connectionist+Bench+(Sonar,+Mines+vs.+Rocks))
- `requirements.txt` – Python dependencies

---
