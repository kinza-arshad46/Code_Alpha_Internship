from flask import Flask, render_template, request
import pandas as pd
import joblib
from utils import predict_price
app = Flask(__name__)
# Load Dataset
df = pd.read_csv("data/car_price_prediction.csv")
# Load Categories
categories = joblib.load("model/categories.pkl")
# Home Page
@app.route("/")
def home():
    stats = {
        "total_cars": len(df),
        "avg_price": int(df["Price"].mean()),
        "max_price": int(df["Price"].max()),
        "min_price": int(df["Price"].min()),
        "avg_airbags": round(df["Airbags"].mean(),1)
    }
    return render_template(
        "index.html",
        categories=categories,
        stats=stats,
        prediction=None
    )
# Prediction
@app.route("/predict", methods=["POST"])
def prediction():
    data = {
        "Levy": request.form["levy"],
        "Manufacturer": request.form["manufacturer"],
        "Model": request.form["model"],
        "Prod. year": int(request.form["year"]),
        "Category": request.form["category"],
        "Leather interior": request.form["leather"],
        "Fuel type": request.form["fuel"],
        "Engine volume": request.form["engine"],
        "Mileage": request.form["mileage"],
        "Cylinders": float(request.form["cylinders"]),
        "Gear box type": request.form["gearbox"],
        "Drive wheels": request.form["drive"],
        "Doors": request.form["doors"],
        "Wheel": request.form["wheel"],
        "Color": request.form["color"],
        "Airbags": int(request.form["airbags"])
    }
    price = predict_price(data)
    stats = {
        "total_cars": len(df),
        "avg_price": int(df["Price"].mean()),
        "max_price": int(df["Price"].max()),
        "min_price": int(df["Price"].min()),
        "avg_airbags": round(df["Airbags"].mean(),1)
    }
    return render_template(
        "index.html",
        categories=categories,
        prediction=price,
        stats=stats
    )
# Run
if __name__ == "__main__":
    app.run(debug=True)