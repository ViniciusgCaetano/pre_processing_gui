import streamlit as st

def Sidebar():
    
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
                       .css-5uatcg{
                         width: 100% !important;
                       }

                      .css-629wbf {
                        width: 100%;
                       }
                       
                    </style>
                    
                    
                """,unsafe_allow_html=True)
    st.sidebar.image("https://i.ibb.co/C2Lxzgd/logo-preprocessing.png") 

    file = st.sidebar.file_uploader('Insert a .XLSX file here')   
    
    st.sidebar.text_area('Applied Changes')
    col1, col2 = st.sidebar.columns(2)
    col1.download_button('Save File', data='fdfd')
    col2.button('Undo last change')
    return file
