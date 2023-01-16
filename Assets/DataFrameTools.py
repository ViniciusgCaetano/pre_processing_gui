import streamlit as st

def dataframe_tools(my_file):
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
    col_1, col_2, col_3, col_4 = st.columns(4)
    col_1.button('+')
    col_2.button('-')
    col_3.button('X')
    col_4.button('/')
    st.number_input('Number')

    return None
