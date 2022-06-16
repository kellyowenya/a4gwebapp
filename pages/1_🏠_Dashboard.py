import pandas as pd
import numpy as np
import datetime
import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# if len(first_name) != 0:
   # st.title("How are you doing, " + first_name + "?")
# else:
   # st.title("Who are you?")
   # st.subheader("Fill out the \"My Info\" page so we can customize your dashboard.")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.write("This page is under construction rn ~ Kelly")
