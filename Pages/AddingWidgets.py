import streamlit as st

st.title("Simple Interest Calculator")

# Inputs 
principal = st.number_input("Enter Principal:", min_value=0.0) 
rate = st.number_input("Interest Rate (%):", min_value=0.0) 
time = st.slider("Time (years):", 1, 10)

# Button 
if st.button("Calculate"): 
    interest = (principal * rate * time) / 100 
    st.success(f"Simple Interest: {interest}")