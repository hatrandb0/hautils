import streamlit as st
import sqlglot

st.set_page_config(
    page_title="🌐 SQL Translation Tool",
    page_icon="🌐",
)

st.write("# SQL Translation Tool 🌐")

dialects = {
    "Trino": "trino",
    "Spark": "spark",
}

with st.form(key='input_form'):
    origin = st.selectbox(
        "Choose original sql dialect:",
        dialects.keys()
            )
    destination = st.selectbox("Choose dialect to translate to:", dialects.keys(), key=1)

    origin_query = st.text_area("Enter query to translate:", placeholder="Original quere goes here, only support one query at a time.", height=300)
    
    to_translate = st.form_submit_button(label='Translate')
    if to_translate:
        dest_query = sqlglot.transpile(origin_query, read=dialects[origin], write=dialects[destination], pretty=True)[0]
        st.divider()
        st.write("## Translated Query:")
        st.code(dest_query, language='sql', line_numbers=True)
