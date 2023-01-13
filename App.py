import streamlit as st
from Assets import Sidebar, DataFrameDisplayer, DataFrameTools
from File import File

st.set_page_config(page_title="Vini's Pre-Processing Tool", page_icon='random', layout="wide")

col1, col2 = st.columns([4, 1])
my_file = File()
Sidebar.Sidebar(my_file)
with col1:
    DataFrameDisplayer.DataFrameDisplayer(my_file)
with col2:
    DataFrameTools.DataFrameTools(my_file)

