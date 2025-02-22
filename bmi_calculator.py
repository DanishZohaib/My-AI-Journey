import streamlit as st
import pandas as pd

st.title("BMI CALCULATOR")

height = st.slider("Enter your height in CM: ", 100, 250, 165)
weight = st.slider("Enter your height in kg: ", 40, 200, 60)

bmi = weight / ((height / 100) **2)

st.write(f"Result: Your BMI is {bmi:.2f}")

st.write("##Compaire your BMI result in below Categories##")
st.write("- Under weight: if your BMI less than 18.5")
st.write("- Normal weight: if your BMI between 18.5 - 24.9")
st.write("- Over weight: if your BMI between 25 - 29.9")


st.write("This application is for practice purpose only Created by Muhammad Danish Zohaib as on 22.02.2025")
