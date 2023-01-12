import streamlit as st
from Assets import Sidebar, DataFrameDisplayer

st.title("Vini's Pre-Processing Tool")
Sidebar.Sidebar()
DataFrameDisplayer.DataFrameDisplayer()