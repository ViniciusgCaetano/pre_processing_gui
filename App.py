import streamlit as st
from Assets import Sidebar, DataFrameDisplayer, DataFrameTools
from file import File

st.set_page_config(page_title="Vini's Pre-Processing Tool", page_icon='random', layout="wide")
st.markdown("""
                    <style>
                        .css-16u8z0w{
                            width: 100%
                        }
                        

                        .css-2ykyy6 {
                            display: none;
                        }
                        
                        .css-hxt7ib{
                            padding-top: 2rem;
                        }
                        
                        
                      .css-z09lfk{
                            width: 100%;
                        }

                       .css-1x8cf1d{
                         width: 100% !important;
                       }
                       
                    </style>
                    
                    
                """,unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])
my_file = File()
Sidebar.Sidebar(my_file)
with col1:
    DataFrameDisplayer.DataFrameDisplayer(my_file)
with col2:
    DataFrameTools.DataFrameTools(my_file)
