import streamlit as st

def DataFrameDisplayer(dataframe=None):
    if not dataframe:
        st.write('No dataframe provided')
        return None
    st.dataframe(dataframe)
    