from io import StringIO
import streamlit as st
import pandas as pd

from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events


st.set_page_config(
    page_title="Crosstab Unpivot",
    page_icon="🧮",
)


read_clipboard = st.button("Paste from clipboard")

if read_clipboard:
    df = pd.read_clipboard()
    st.write(df)