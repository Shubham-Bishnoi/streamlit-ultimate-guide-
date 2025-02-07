import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Hello, Let's Strat with Streamlit ")
st.write("Yes, it is!")

if st.button("Click me"):
    st.write("Button clicked! 🚀")

name = st.text_input("Enter your name")
age = st.slider("Select your age", 1, 100)

st.write(f"Hello {name}, you are {age} years old! 🎂")

st.title("Matplotlib Chart 📊")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="Sine Wave", color="blue")
ax.set_xlabel("X values")
ax.set_ylabel("sin(x)")
ax.legend()

st.pyplot(fig)

import streamlit as st
import pandas as pd

st.title("DataFrame Example")

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 78]
})

st.write(df)  # Basic table
st.dataframe(df)  # Interactive table

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

