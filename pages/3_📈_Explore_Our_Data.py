import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(
    page_title="Explore Our Data",
    page_icon="📈",
)

data_page = st.container()

with data_page:
    st.write("Here's a bunch of sample data for a placeholder, when we have our real datasets, I'll arrange them along with a nice user-friendly description of what they do/why they're relevant.")
    
    df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

    st.dataframe(df)  # Same as st.write(df)

    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.area_chart(chart_data)

    chart_data1 = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

    st.bar_chart(chart_data1)

