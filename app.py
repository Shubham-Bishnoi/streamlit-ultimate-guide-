import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
import requests
import cv2
from PIL import Image
from io import BytesIO
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Ultimate Streamlit App", layout="wide")

st.title("🚀 Streamlit Ultimate Guide App")
st.write("This is a complete demonstration of Streamlit functionalities.")

name = st.text_input("Enter your name")
age = st.slider("Select your age", 1, 100)
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old!")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Charts", "Machine Learning", "File Upload", "API Fetch"])

if page == "Charts":
    st.subheader("📊 Data Visualization")
    df = pd.DataFrame(np.random.randn(100, 3), columns=["A", "B", "C"])
    st.dataframe(df)
    
    fig, ax = plt.subplots()
    sns.histplot(df["A"], bins=20, kde=True, ax=ax)
    st.pyplot(fig)
    
    fig2 = px.scatter(df, x="A", y="B", size="C", color="C", title="Plotly Scatter Plot")
    st.plotly_chart(fig2)
    
    chart = alt.Chart(df).mark_circle(size=60).encode(
        x="A", y="B", color="C", tooltip=["A", "B", "C"]
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

elif page == "Machine Learning":
    st.subheader("🤖 Machine Learning Model")
    X = np.array(range(1, 21)).reshape(-1, 1)
    y = X.ravel() * 3 + np.random.randint(0, 10, size=20)
    model = LinearRegression()
    model.fit(X, y)
    pred_y = model.predict(X)
    
    fig, ax = plt.subplots()
    ax.scatter(X, y, color="blue", label="Actual Data")
    ax.plot(X, pred_y, color="red", label="Predicted Line")
    ax.legend()
    st.pyplot(fig)

elif page == "File Upload":
    st.subheader("📂 File Upload")
    uploaded_file = st.file_uploader("Upload a CSV or Image", type=["csv", "jpg", "png"])
    
    if uploaded_file is not None:
        if uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
            st.write(df)
        else:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

elif page == "API Fetch":
    st.subheader("🌍 Fetching Data from API")
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to fetch data from API")

st.sidebar.write("---")
st.sidebar.write("🔥 **Powered by Streamlit**")
