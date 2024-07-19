from pandasai.llm.local_llm import LocalLLM
llm = LocalLLM(
    api_base = "http://localhost:11434/v1",
    model = "phi3"
)

import streamlit as st
st.title("Employee data analysis using Microsoft Phi3")

import pandas as pd
from pandasai import SmartDataframe
uploaded_file = st.file_uploader("Upload your employees csv file", type=['csv'])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())
    
    df = SmartDataframe(data, config={"llm": llm})
    prompt = st.text_area("Enter your question:")
    if st.button("Answer"):
        if prompt:
            with st.spinner("Working on it..."):
                st.write(df.chat(prompt))
    