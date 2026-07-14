import joblib
import pandas as pd
import numpy as np

# ===============================
# Load Saved Files
# ===============================

model = joblib.load("model/car_price_prediction_model.pkl")

scaler = joblib.load("model/scaler.pkl")

feature_columns = joblib.load("model/feature_columns.pkl")

categories = joblib.load("model/categories.pkl")


# ===============================
# Clean Levy
# ===============================

def clean_levy(value):

    try:
        return float(value)

    except:
        return np.nan


# ===============================
# Clean Mileage
# ===============================

def clean_mileage(value):

    value = str(value).replace("km", "")

    value = value.replace(",", "")

    value = value.strip()

    return int(value)


# ===============================
# Clean Engine Volume
# ===============================

def clean_engine(value):

    value = str(value)

    value = value.replace("Turbo", "")

    value = value.strip()

    return float(value)


# ===============================
# Prepare Data
# ===============================

def prepare_input(data):

    df = pd.DataFrame([data])

    df["Levy"] = df["Levy"].apply(clean_levy)

    df["Mileage"] = df["Mileage"].apply(clean_mileage)

    df["Engine volume"] = df["Engine volume"].apply(clean_engine)

    df.fillna(0, inplace=True)

    df = pd.get_dummies(df)

    df = df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    return df


# ===============================
# Prediction Function
# ===============================

def predict_price(data):

    prepared = prepare_input(data)

    prediction = model.predict(prepared)

    return round(prediction[0], 2)