# 🚗 Car Price Prediction using Machine Learning

## 📖 Overview

This project is an end-to-end Machine Learning application that predicts the estimated price of a car based on multiple vehicle characteristics. It covers the complete machine learning pipeline, from data preprocessing and exploratory data analysis (EDA) to model training, evaluation, and deployment using Flask.

The goal of this project is to demonstrate how machine learning techniques can be applied to solve a real-world price prediction problem.

---

## ✨ Features

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Multiple Regression Models

  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor
* Model Evaluation
* Flask Web Dashboard
* Interactive Car Price Prediction
* Model Saving with Joblib

---

## 📂 Project Structure

```text
Car_Price_Prediction/
│
├── app.py
├── utils.py
├── requirements.txt
│
├── model/
│   ├── car_price_prediction_model.pkl
│   ├── scaler.pkl
│   ├── feature_columns.pkl
│   └── categories.pkl
│
├── data/
│   └── car_price_dataset.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
└── README.md
```

---

## 📊 Dataset Features

The prediction model uses the following vehicle information:

* Manufacturer
* Model
* Production Year
* Category
* Fuel Type
* Engine Volume
* Mileage
* Cylinders
* Gear Box Type
* Drive Wheels
* Leather Interior
* Doors
* Wheel Position
* Color
* Airbags
* Levy

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Flask
* Joblib
* HTML
* CSS
* JavaScript

---

## 🤖 Machine Learning Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Data Preprocessing
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Prediction
10. Flask Dashboard Deployment

---

## 📈 Model Evaluation Metrics

The models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

Among the trained models, **Random Forest Regressor** delivered the best predictive performance and was selected as the final model.

---

## 🚀 Dashboard

The Flask dashboard allows users to:

* Enter vehicle information
* Predict estimated car prices
* View project statistics
* Explore a clean and user-friendly interface

---

## 💡 Learning Outcomes

This project strengthened my understanding of:

* Data preprocessing
* Feature engineering
* Regression algorithms
* Model evaluation
* Flask application development
* Machine Learning deployment

---

## 📬 Connect With Me

I enjoy building practical Machine Learning and Data Science projects while continuously improving my skills.

If you have suggestions or feedback, feel free to connect with me.
