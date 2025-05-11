import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model_xg.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📊 Customer Churn Prediction Dashboard")

st.markdown("Fill in the customer details to predict if they are likely to churn.")

# Sidebar input fields
gender = st.sidebar.selectbox("Gender", ['Female', 'Male'])
seniorcitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Has Partner", [0, 1])
dependents = st.sidebar.selectbox("Has Dependents", [0, 1])
tenure = st.sidebar.slider("Tenure (months)", 0, 72, 2)
phoneservice = st.sidebar.selectbox("Phone Service", [0, 1])
paperlessbilling = st.sidebar.selectbox("Paperless Billing", [0, 1])
monthlycharges = st.sidebar.number_input("Monthly Charges", 0.0, 500.0, 53.85)
totalcharges = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 108.15)
monthlychargepertenure = st.sidebar.number_input("Monthly Charge per Tenure", 0.0, 1000.0, 17.95)

# One-hot encoded selections
multiplelines = st.sidebar.selectbox("Multiple Lines", [
    "No phone service", "No", "Yes"
])
internetservice = st.sidebar.selectbox("Internet Service", [
    "DSL", "Fiber optic", "No"
])
onlinesecurity = st.sidebar.selectbox("Online Security", [
    "No", "Yes", "No internet service"
])
onlinebackup = st.sidebar.selectbox("Online Backup", [
    "No", "Yes", "No internet service"
])
deviceprotection = st.sidebar.selectbox("Device Protection", [
    "No", "Yes", "No internet service"
])
techsupport = st.sidebar.selectbox("Tech Support", [
    "No", "Yes", "No internet service"
])
streamingtv = st.sidebar.selectbox("Streaming TV", [
    "No", "Yes", "No internet service"
])
streamingmovies = st.sidebar.selectbox("Streaming Movies", [
    "No", "Yes", "No internet service"
])
contract = st.sidebar.selectbox("Contract Type", [
    "Month-to-month", "One year", "Two year"
])
paymentmethod = st.sidebar.selectbox("Payment Method", [
    "Bank transfer (automatic)", "Credit card (automatic)",
    "Electronic check", "Mailed check"
])
tenuregroup = st.sidebar.selectbox("Tenure Group", [
    "Regular", "Loyal", "New"
])

# Constructing the input dictionary
input_dict = {
    'gender': 1 if gender == 'Male' else 0,
    'seniorcitizen': seniorcitizen,
    'partner': partner,
    'dependents': dependents,
    'tenure': tenure,
    'phoneservice': phoneservice,
    'paperlessbilling': paperlessbilling,
    'monthlycharges': monthlycharges,
    'totalcharges': totalcharges,
    'monthlychargepertenure': monthlychargepertenure,

    # One-hot encodings
    'multiplelines_No phone service': 1 if multiplelines == "No phone service" else 0,
    'multiplelines_Yes': 1 if multiplelines == "Yes" else 0,

    'internetservice_Fiber optic': 1 if internetservice == "Fiber optic" else 0,
    'internetservice_No': 1 if internetservice == "No" else 0,

    'onlinesecurity_No internet service': 1 if onlinesecurity == "No internet service" else 0,
    'onlinesecurity_Yes': 1 if onlinesecurity == "Yes" else 0,

    'onlinebackup_No internet service': 1 if onlinebackup == "No internet service" else 0,
    'onlinebackup_Yes': 1 if onlinebackup == "Yes" else 0,

    'deviceprotection_No internet service': 1 if deviceprotection == "No internet service" else 0,
    'deviceprotection_Yes': 1 if deviceprotection == "Yes" else 0,

    'techsupport_No internet service': 1 if techsupport == "No internet service" else 0,
    'techsupport_Yes': 1 if techsupport == "Yes" else 0,

    'streamingtv_No internet service': 1 if streamingtv == "No internet service" else 0,
    'streamingtv_Yes': 1 if streamingtv == "Yes" else 0,

    'streamingmovies_No internet service': 1 if streamingmovies == "No internet service" else 0,
    'streamingmovies_Yes': 1 if streamingmovies == "Yes" else 0,

    'contract_One year': 1 if contract == "One year" else 0,
    'contract_Two year': 1 if contract == "Two year" else 0,

    'paymentmethod_Credit card (automatic)': 1 if paymentmethod == "Credit card (automatic)" else 0,
    'paymentmethod_Electronic check': 1 if paymentmethod == "Electronic check" else 0,
    'paymentmethod_Mailed check': 1 if paymentmethod == "Mailed check" else 0,

    'tenuregroup_Loyal': 1 if tenuregroup == "Loyal" else 0,
    'tenuregroup_New': 1 if tenuregroup == "New" else 0
}

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

st.write("### 📋 Input Data")
st.dataframe(input_df)

# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Prediction: {'Churn' if prediction == 1 else 'No Churn'}")