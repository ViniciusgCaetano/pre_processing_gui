import streamlit as st

def DataFrameTools(my_file):
    if not my_file.is_full:
        return False
    
    columns = my_file.get_file().columns.values
    column_name = st.selectbox('Column', columns)
    st.header('Actions')

    if st.button('Delete Column'):
        my_file.delete_column(column_name)
    
    st.subheader('Text Functions')
    st.button('Capitalize')
    st.button('Lowercase')
    st.button('Uppercase')

    st.subheader('Filter Functions')
    st.button('Delete empty rows')

    st.subheader('Number functions')
    b1, b2, b3, b4 = st.columns(4)
    b1.button('+')
    b2.button('-')
    b3.button('X')
    b4.button('/')
    st.number_input('Number')
    




    return None



    