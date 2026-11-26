import streamlit as st
import pandas as pd
import joblib

# 1. Wide layout එක දාමු
st.set_page_config(page_title="SL Vehicle Price Predictor", page_icon="🚗", layout="wide")

# 2. උඩ හිස් ඉඩ අඩු කරලා සම්පූර්ණ UI එකම එක screen එකකට ගන්න CSS
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 1rem;
            max-width: 1100px;
        }
    </style>
""", unsafe_allow_html=True)

# Model, Columns, සහ Brand-Model mapping load කිරීම
model = joblib.load('sl_vehicle_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')
brand_models = joblib.load('brand_models.pkl')

brands = sorted(list(brand_models.keys()))
towns = sorted([col.replace('Town_', '') for col in model_columns if col.startswith('Town_')])

st.markdown("## 🚗 Sri Lankan Used Vehicle Price Predictor")
st.caption("Machine Learning (Random Forest) මගින් ශ්‍රී ලංකාවේ වාහන මිල ගණන් පුරෝකථනය කිරීම.")
st.divider()

# 3. Columns 3කට බෙදමු — එතකොට scroll කරන්නේ නැතුව ඔක්කොම එකපාර පේනවා!
col1, col2, col3 = st.columns(3)

with col1:
    brand = st.selectbox("Brand (වාහන වර්ගය)", brands)
    available_models = brand_models[brand]
    model_name = st.selectbox("Model (මාදිලිය)", available_models)
    yom = st.number_input("Year of Manufacture (වර්ෂය)", min_value=1960, max_value=2025, value=2018)
    engine_cc = st.number_input("Engine Capacity (cc)", min_value=600, max_value=5000, value=1500, step=50)

with col2:
    mileage = st.number_input("Mileage (KM)", min_value=0, max_value=800000, value=85000, step=1000)
    gear = st.selectbox("Transmission (Gear)", ["Automatic", "Manual"])
    fuel_type = st.selectbox("Fuel Type (ඉන්ධන වර්ගය)", ["Petrol", "Diesel", "Hybrid", "Electric"])
    town = st.selectbox("Town (නගරය)", towns)

with col3:
    condition = st.selectbox("Condition", ["USED", "NEW"])
    leasing = st.selectbox("Leasing Status", ["No Leasing", "Ongoing Lease"])
    options_count = st.slider("Available Options (A/C, Power Steering, Mirror, Window)", 0, 4, 4)
    st.write("") # පොඩි ඉඩක් තියන්න
    predict_btn = st.button("Predict Vehicle Price 💰", type="primary", width="stretch")

# Button එක click කළාම result එක පහළින් ලස්සනට පෙන්නනවා
if predict_btn:
    input_data = pd.DataFrame(columns=model_columns)
    input_data.loc[0] = 0
    
    input_data['Engine (cc)'] = engine_cc
    input_data['Gear'] = 1 if gear == 'Automatic' else 0
    input_data['Millage(KM)'] = mileage
    input_data['Leasing'] = 1 if leasing == 'Ongoing Lease' else 0
    input_data['Condition'] = 1 if condition == 'NEW' else 0
    input_data['Vehicle_Age'] = 2025 - yom
    input_data['Options_Count'] = options_count
    
    for col_name in [f"Brand_{brand}", f"Model_{model_name}", f"Fuel Type_{fuel_type}", f"Town_{town}"]:
        if col_name in input_data.columns:
            input_data[col_name] = 1
            
    prediction = model.predict(input_data)[0]
    st.success(f"### ඇස්තමේන්තුගත වෙළඳපොළ මිල: රු. ලක්ෂ {prediction:,.2f}  *(ආසන්න වශයෙන් රු. {prediction * 100000:,.0f})*")