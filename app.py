import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("Model (7).pkl", "rb"))

st.set_page_config(page_title="ML Predictor", layout="centered")

st.title("🚀 Machine Learning Predictor")
st.write("Enter input values below to get predictions.")

# Example input fields (EDIT based on your model features)
# Replace these with actual feature names
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

# Convert inputs into array
input_data = np.array([[feature1, feature2, feature3]])

# Predict button
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        st.success(f"Prediction: {prediction[0]}")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("Built with Streamlit ❤️")
