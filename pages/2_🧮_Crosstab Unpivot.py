from io import StringIO
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Crosstab Unpivot",
    page_icon="🧮",
)


st.write('# Crosstab Unpivot')

delimiters = {
    'Tab': '\t',
    'Comma (,)': ',',
    'Semi-colon (;)': ';'

}


dim = st.selectbox(
    'Column delimiter',
    delimiters.keys()
    )


st.write("Please first copy data from your file or sample https://docs.google.com/spreadsheets/d/17RDKTnwQuWd-kL7YdR2XZ1dvcj5nSEdhOrz3F02Z9No")

with st.expander("Paste your data here", expanded=True):
    data_str = st.text_area("Paste data below", label_visibility="collapsed")


if data_str:
    df = pd.read_csv(StringIO(data_str), delimiter=delimiters[dim])
    st.write("Original crosstab")
    st.dataframe(df)
    with st.sidebar()
        id_vars = st.multiselect("ID columns", df.columns)
        value_vars = st.multiselect('Value columns', df.columns)
    if id_vars and value_vars:
        df_unpivot = pd.melt(df, id_vars=id_vars, value_vars=value_vars)
        st.write('Unpivoted')
        st.dataframe(df_unpivot)