import streamlit as st
import pandas as pd
import openpyxl

def DataFrameDisplayer(dataframe=None):
    if not dataframe:
        st.header('No dataframe provided')
        return None
    df = pd.read_excel(dataframe)
    st.subheader('First 10 rows')
    st.dataframe(df.head(10), use_container_width=True)
    