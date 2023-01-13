import streamlit as st
from Assets import Sidebar, DataFrameDisplayer
st.set_page_config(page_title="Vini's Pre-Processing Tool", page_icon='random', layout="wide")

file = Sidebar.Sidebar()
DataFrameDisplayer.DataFrameDisplayer(file)