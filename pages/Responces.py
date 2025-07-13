import streamlit as st
import pandas as pd
import os

st.title("Survey Results")

filename = "apple_surveys.csv"

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    try:
        df = pd.read_csv(filename)
        if df.empty:
            st.write("No survey results found.")
        else:
            st.dataframe(df)
    except Exception:
        st.write("Error reading survey data.")
else:
    st.write("No survey results found.")