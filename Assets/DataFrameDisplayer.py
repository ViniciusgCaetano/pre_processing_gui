import streamlit as st
import pandas as pd
import openpyxl

def DataFrameDisplayer(my_file):

    if not my_file.is_full:
        st.header('No dataframe provided')
        return None

    df = my_file.get_file()
    st.subheader('First 10 rows')
    st.dataframe(df.head(10), use_container_width=True)
    
    