# 🚗 Sri Lankan Used Vehicle Price Predictor

An end-to-end Machine Learning web application that predicts used vehicle prices in Sri Lanka using **Random Forest Regression** and **Streamlit**.

## 📊 Project Highlights
- **Dataset:** 9,500+ Sri Lankan vehicle listings (`Brand`, `Model`, `YOM`, `Engine CC`, `Gear`, `Fuel Type`, `Mileage`, `Town`, etc.).
- **Data Cleaning & Feature Engineering:**
  - Removed duplicate listings and standardized inconsistent text entries.
  - Engineered domain-specific features: `Vehicle_Age` and `Options_Count`.
  - Grouped rare categories into `OTHER`, reducing `Model` cardinality from 1,555 to 134 to prevent overfitting.
  - Built dependent dropdowns (`brand_models.pkl`) so users can only select valid models for a chosen brand.
- **Model Performance Comparison:**
  - **Linear Regression:** $R^2 = 0.7551$ | MAE = 11.13 Lakhs
  - **Random Forest Regressor:** $R^2 = 0.9015$ | MAE = 5.72 Lakhs

## 🛠️ Tech Stack
- **Language:** Python
- **Data Processing & ML:** Pandas, NumPy, Scikit-Learn, Joblib
- **Web Framework:** Streamlit

## 🚀 How to Run Locally
```bash
git clone [https://github.com/NavinduDilshan48/SL-Vehicle-Price-Predictor.git](https://github.com/NavinduDilshan48/SL-Vehicle-Price-Predictor.git)
cd SL-Vehicle-Price-Predictor
pip install -r requirements.txt
streamlit run app.py