# import streamlit as st

# # Page Title
# st.title("Welcome Abhinav")

# # Subtitle
# st.header("My First Streamlit App")

# # Text
# st.write("This is a simple Streamlit page.")

# # User Input
# name = st.text_input("Enter your name:")

# if name:
#     st.success(f"Hello {name}, welcome to Streamlit! 🚀")

# # Button
# if st.button("Click Me"):
#     st.balloons()
# train_model.py

import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

st.title("⚡ Simple AI Model (Runs Instantly)")

# Small built-in dataset
X = np.array([[1,2],[2,3],[3,4],[5,6],[6,7],[7,8]])
y = np.array([0,0,0,1,1,1])

# Train tiny model (very fast)
model = LogisticRegression()
model.fit(X, y)

st.write("Enter two numbers to predict class (0 or 1)")

num1 = st.number_input("Number 1", value=1.0)
num2 = st.number_input("Number 2", value=2.0)

if st.button("Predict"):
    prediction = model.predict([[num1, num2]])
    st.success(f"Prediction: {prediction[0]}")