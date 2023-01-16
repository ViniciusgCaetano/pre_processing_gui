import streamlit as st
import streamlit_nested_layout

def DataFrameDisplayer(my_file):

    if not my_file.is_full:
        st.header('No file provided')
        return None

    df = my_file.get_file()
    st.subheader('First 10 rows')
    st.dataframe(df.head(10), use_container_width=True)

    with st.expander('Summary', expanded=True):
        st.title('Summary')
        col1, col2, col3 = st.columns(3)
        col1.subheader(f'Rows: {df.shape[0]}')
        col2.subheader(f'Columns: {df.shape[1]}')
        col3.subheader('Empty rows: 0')
    