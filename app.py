import streamlit as st
import pandas as pd
from model_utils import predict_delivery_time

st.title("🚚 Delivery Time Prediction")

route_type = st.selectbox("Route Type", ["FTL", "Carting"])
osrm_time = st.number_input("OSRM Time (minutes)", min_value=1.0, value=180.0)
osrm_distance = st.number_input("OSRM Distance (km)", min_value=1.0, value=120.0)

trip_creation_time = st.text_input("Trip Creation Time", "2026-01-23 18:04")
od_start_time = st.text_input("OD Start Time", "2026-01-23 18:30")
od_end_time = st.text_input("OD End Time", "2026-01-23 23:00")

if st.button("Predict Delivery Time"):
    input_df = pd.DataFrame([{
        "route_type": route_type,
        "osrm_time": osrm_time,
        "osrm_distance": osrm_distance,
        "trip_creation_time": trip_creation_time,
        "od_start_time": od_start_time,
        "od_end_time": od_end_time
    }])

    prediction = predict_delivery_time(input_df)

    st.success(f"⏱️ Predicted Delivery Time: **{round(prediction, 2)} minutes**")
