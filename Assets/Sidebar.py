import streamlit as st

def sidebar(my_file):

    st.sidebar.image("https://i.ibb.co/C2Lxzgd/logo-preprocessing.png")

    file = st.sidebar.file_uploader('Insert a .XLSX file here')
    if file:
        my_file.read_excel(file)

    st.sidebar.text_area('Applied Changes')
    col1, col2 = st.sidebar.columns(2)
    col1.download_button('Save File', data='fdfd')
    col2.button('Undo last change')
