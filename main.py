import streamlit as st
import pandas as pd

st.title("My Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Convert Date column to datetime format
    df["Date"] = pd.to_datetime(df["Date"])

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]

    if filtered_df.empty:
        st.warning("No matching data found for the selected filter!")
    else:
        st.write(filtered_df)

        st.subheader("Plot Data")
        x_column = st.selectbox("Select X-axis column", ["Date"])  # Restrict to Date
        y_column = st.selectbox("Select Y-axis column", ["Sales", "Revenue"])  # Only numeric

        if st.button("Generate Plot"):
            if y_column in filtered_df.columns:
                # Ensure the DataFrame has data and Date is set as index
                filtered_df = filtered_df.set_index("Date")  # Set Date as index
                st.line_chart(filtered_df[[y_column]])  # Ensure Y-axis column is selected
            else:
                st.error("Selected Y-axis column is not available in the dataset.")
else:
    st.write("Waiting for file upload...")
