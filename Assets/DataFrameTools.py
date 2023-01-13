import streamlit as st

def DataFrameTools(my_file):
    if not my_file.is_full:
        return False
    
    columns = my_file.get_file().columns.values
    column_name = st.selectbox('Column', columns)
    if st.button('Delete Column'):
        my_file.delete_column(column_name)
        
    return None



    