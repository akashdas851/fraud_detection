import streamlit as st
import pandas as pd 
import joblib 
model = joblib.load("fraud_detection_model.pkl")
st.title("Fraud Detection Model")

st.markdown("please enter the transaction detail and use the predict button")
st.divider()

transaction_type=st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount=st.number_input("Amount", min_value=0.0, value =1000.0)
oldbalanceOrg=st.number_input("Old Balance (sender)", min_value=0.0, value =10000.0)
newbalanceorig=st.number_input("New Balance (sender)", min_value=0.0, value =9000.0)
oldbalanceDest=st.number_input("Old Balance (receiver)", min_value=0.0, value =0.0)
newbalancedest=st.number_input("New Balance (receiver)", min_value=0.0, value =1000.0)

if st.button("Predict"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig":newbalanceorig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalancedest
    }])

    prediction=model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction==1:
        st.error("The transaction is Fraudulent or can be fraud ")
    else:
        st.success("The transaction is Legitimate which mean it look like it is not fraud")

# test change