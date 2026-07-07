import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction")

st.header("Enter Customer Details")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=1)
monthlycharges = st.number_input("Monthly Charges", min_value=0.0)
totalcharges = st.number_input("Total Charges", min_value=0.0)

# Encoding
gender_Female = 1 if gender == "Female" else 0
gender_Male = 1 if gender == "Male" else 0

Partner_Yes = 1 if partner == "Yes" else 0
Dependents_Yes = 1 if dependents == "Yes" else 0

# Default values for remaining dummy variables
PhoneService_Yes = 1
MultipleLines_No = 1
StreamingTV_Yes = 0
StreamingMovies_No = 1
StreamingMovies_Yes = 0
Contract_One_year = 0
Contract_Two_year = 0
PaperlessBilling_Yes = 1
PaymentMethod_Credit_card_automatic = 0
PaymentMethod_Electronic_check = 1
PaymentMethod_Mailed_check = 0

# Prediction
if st.button("Predict Churn"):

    input_data = pd.DataFrame([[
        senior,
        tenure,
        monthlycharges,
        totalcharges,
        gender_Female,
        gender_Male,
        Partner_Yes,
        Dependents_Yes,
        PhoneService_Yes,
        MultipleLines_No,
        StreamingTV_Yes,
        StreamingMovies_No,
        StreamingMovies_Yes,
        Contract_One_year,
        Contract_Two_year,
        PaperlessBilling_Yes,
        PaymentMethod_Credit_card_automatic,
        PaymentMethod_Electronic_check,
        PaymentMethod_Mailed_check
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠ Customer is likely to Churn.")
    else:
        st.success("✅ Customer is likely to Stay.")