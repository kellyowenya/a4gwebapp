import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.session_state.active_page = st.session_state.active_page
st.session_state.first = st.session_state.first

st.set_page_config(
    page_title="My Info",
    page_icon="🧑",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.header("Information")
st.sidebar.markdown(
    """We use both **personal** (name, age) and **biological** information
    like your height and weight to make sure this app can best suit your needs!
    Then, we'll need information about the medication you're taking so we can 
    fully customize your experience.
    *Don't worry, you can change this information at any time, and everything will
    adjust accordingly.*"""
)

st.header("Tell us a bit about yourself.")
def form_callback():
    # st.write(st.session_state.first)
    st.session_state.first = st.session_state.first

with st.form("user_info"):
    
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name", max_chars=20, key="first")
    with col2:
        last_name = st.text_input("Last Name", max_chars=20)
    
    gender = st.radio("What's your gender?", ("Male", "Female"), help="If you identify as a different gender than the one assigned to you at birth, please put your birth gender here.", horizontal=True)
    user_dob = st.date_input("When's your birthday?", min_value=datetime.date(1910, 1, 1))
    height = st.slider('How tall are you?', 100, 250, 175, format="%d cm")
    weight = st.slider('How much do you weigh?', 35, 150, 75, format="%d kg")
    st.subheader("Where do you live?")
    st.markdown("*Your exact location is important, as we use location-specific data to assess your personal situation and risk level. More info found in the \"Explore Our Data\" page.*")
    st.map()

    st.header("Now, about your medicine intake.")
    options = st.multiselect("What opioid medications or drugs are you currently taking?",
    ["Codeine", "Oxycodone", "Morphine", "Hydromorphone", "Fentanyl", "Heroin", "Methadone", "Buprenorphine"], help="You can select more than one off of this list.")
    column1, column2, column3 = st.columns(3)
    with column1:
        addiction_status = st.radio("Are you currently in treatment for any addiction?", ("Yes", "No"))
    with column2:
        overdose_status = st.radio("Have you previously overdosed on any drug?", ("Yes", "No"))
    with column3:
        prev_hospital_status = st.radio("Have you been hospitalized in the past 6 months?", ("Yes", "No"))
    dosage_time = st.time_input("At what time do you usually prefer to take your prescription medication?", datetime.time(9, 00))
    
    st.write("That's all we need from you right now!")
    st.markdown("*Head over to your customized Dashboard to see our analysis at work.*")
    st.form_submit_button("Submit and take me there", on_click=form_callback)


    