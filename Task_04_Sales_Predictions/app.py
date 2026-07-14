from flask import Flask, render_template, request
import pandas as pd
import joblib

# ==========================================
# Initialize Flask App
# ==========================================

app = Flask(__name__)

# ==========================================
# Load Saved Files
# ==========================================

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("label_encoders.pkl")


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# Prediction Route
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ==================================
        # Get User Inputs
        # ==================================

        tv_ads = float(request.form["tv_ads"])
        social_ads = float(request.form["social_ads"])
        google_ads = float(request.form["google_ads"])

        marketing_budget = float(request.form["marketing_budget"])

        previous_sales = float(request.form["previous_sales"])

        discount = float(request.form["discount"])

        platform = request.form["platform"]
        target = request.form["target"]
        region = request.form["region"]
        season = request.form["season"]

        # ==================================
        # Encode Categorical Values
        # ==================================

        platform_encoded = encoders["Platform"].transform([platform])[0]

        target_encoded = encoders["Target_Audience"].transform([target])[0]

        region_encoded = encoders["Region"].transform([region])[0]

        season_encoded = encoders["Season"].transform([season])[0]

        # ==================================
        # Create DataFrame
        # ==================================

        input_data = pd.DataFrame({

            "TV_Ads": [tv_ads],

            "Social_Media_Ads": [social_ads],

            "Google_Ads": [google_ads],

            "Platform": [platform_encoded],

            "Target_Audience": [target_encoded],

            "Region": [region_encoded],

            "Season": [season_encoded],

            "Discount": [discount],

            "Marketing_Budget": [marketing_budget],

            "Previous_Sales": [previous_sales]

        })

        # ==================================
        # Scale Data
        # ==================================

        scaled_data = scaler.transform(input_data)

        # ==================================
        # Prediction
        # ==================================

        prediction = model.predict(scaled_data)

        predicted_sales = round(float(prediction[0]), 2)

        # ==================================
        # Performance Rating
        # ==================================

        if predicted_sales >= 800:

            performance = "Excellent"

            suggestion = (
                "Excellent campaign potential. Increase advertising investment "
                "to maximize revenue."
            )

        elif predicted_sales >= 600:

            performance = "Good"

            suggestion = (
                "Campaign performance looks good. Increasing social media "
                "marketing may further improve sales."
            )

        elif predicted_sales >= 400:

            performance = "Average"

            suggestion = (
                "Campaign is performing moderately. Optimize your target "
                "audience and marketing budget."
            )

        else:

            performance = "Low"

            suggestion = (
                "Predicted sales are low. Review your advertising strategy, "
                "platform selection, and customer targeting."
            )

        # ==================================
        # Render Result Page
        # ==================================

        return render_template(

            "result.html",

            prediction=predicted_sales,

            performance=performance,

            suggestion=suggestion,

            tv_ads=tv_ads,

            social_ads=social_ads,

            google_ads=google_ads,

            marketing_budget=marketing_budget,

            previous_sales=previous_sales,

            discount=discount,

            platform=platform,

            target=target,

            region=region,

            season=season

        )

    except Exception as e:

        return f"<h2>Error:</h2><p>{e}</p>"


# ==========================================
# Run Flask App
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)