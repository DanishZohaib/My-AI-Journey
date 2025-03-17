import streamlit as st

st.title("Unit Converter")
st.write("Created by Danish Zohaib")

units = {
    "Meters": 1,
    "Kilometers": 0.001,
    "Centimeters": 100,
    "Inches": 39.3701,
    "Feet": 3.28084,
    "Miles": 0.000621371
}

# User input
amount = st.number_input("Enter value", min_value=0.0, format="%.4f")
from_unit = st.selectbox("From", list(units.keys()))
to_unit = st.selectbox("To", list(units.keys()))

def convert_length(value, from_unit, to_unit):
    return value * (units[to_unit] / units[from_unit])

if st.button("Convert"):
    result = convert_length(amount, from_unit, to_unit)
    st.success(f"Result: {result:.4f} {to_unit}")