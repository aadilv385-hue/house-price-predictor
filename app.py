import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Training Data
data = {
    "Area": [1000, 1500, 2000, 2500, 3000],
    "Price": [200000, 300000, 400000, 500000, 600000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Input and Output
X = df[["Area"]]
y = df["Price"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("House Price Predictor")

st.write("Enter house area below")

area = st.number_input("Area in sq ft", min_value=500)

# Predict Button
if st.button("Predict Price"):
    prediction = model.predict([[area]])

    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")