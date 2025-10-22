
import streamlit as st
import pandas as pd
import joblib


model = joblib.load("trained/calories_model.joblib")

st.title("Calories Burned Predictor")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age (years)", 10, 100, 24)
height = st.number_input("Height (cm)", 120.0, 230.0, 170.0)
weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
duration = st.number_input("Workout Duration (minutes)", 1.0, 30.0, 30.0)  
heart_rate = st.number_input("Average Heart Rate (bpm)", 40.0, 220.0, 120.0)
body_temp = st.number_input("Body Temperature (°C)", 35.0, 42.5, 37.0)


if gender == "Male":
    gender_num = 1
else:
    gender_num = 0

data = pd.DataFrame({
    "Gender": [gender_num],
    "Age": [age],
    "Height": [height],
    "Weight": [weight],
    "Duration": [duration],
    "Heart_Rate": [heart_rate],
    "Body_Temp": [body_temp]
}, columns=["Gender", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"])

if st.button("Estimate Calories"):
    result = model.predict(data)
    answer = result[0]
    st.write(" **Estimated Calories Burned:**", round(answer, 0), "kcal")
