import streamlit as st
import datetime

if 'active_page' not in st.session_state:
    st.session_state.active_page = "Welcome"
    st.session_state.first = ""
    st.session_state.last = ""
    st.session_state.prev_hosp = "Yes"

if "blood" not in st.session_state:
    st.session_state.blood = "Unknown"

if 'dob' not in st.session_state:
    st.session_state.dob = datetime.date(1990, 1, 1)

if "height" not in st.session_state:
    st.session_state.height = 175

if "weight" not in st.session_state:
    st.session_state.weight = 75

if "current_drugs" not in st.session_state:
    st.session_state.current_drugs = []

if "prev_overdose" not in st.session_state:
    st.session_state.prev_overdose = "Yes"

if "prev_hosp" not in st.session_state:
    st.session_state.prev_hosp = "Yes"

if "contact_first" not in st.session_state:
    st.session_state.contact_first = ""

if "contact_phone" not in st.session_state:
    st.session_state.contact_phone = ""

if "kit_boolean" not in st.session_state:
    st.session_state.kit_boolean = "No"

if "kit_location" not in st.session_state:
    st.session_state.kit_location = ""

if "gender" not in st.session_state:
    st.session_state.gender = "Male"

if "fam_sub_abuse" not in st.session_state:
    st.session_state.fam_sub_abuse = []

if "per_disord" not in st.session_state:
    st.session_state.per_disord= "Yes"

if "prev_abuse" not in st.session_state:
    st.session_state.prev_abuse = "Yes"

if "depression" not in st.session_state:
    st.session_state.depression = "Yes"

if "past_sub_abuse" not in st.session_state:
    st.session_state.past_sub_abuse = []

if "addiction" not in st.session_state:
    st.session_state.addiction = "Yes"

if "dose_time" not in st.session_state:
    st.session_state.dose_time = datetime.time(9, 00)

st.session_state.active_page = st.session_state.active_page
st.session_state.first = st.session_state.first
st.session_state.last = st.session_state.last
st.session_state.dob = st.session_state.dob
st.session_state.blood = st.session_state.blood
st.session_state.height = st.session_state.height
st.session_state.weight = st.session_state.weight
st.session_state.current_drugs = st.session_state.current_drugs
st.session_state.prev_overdose =  st.session_state.prev_overdose
st.session_state.prev_hosp =  st.session_state.prev_hosp
st.session_state.contact_first = st.session_state.contact_first
st.session_state.contact_phone = st.session_state.contact_phone
st.session_state.kit_boolean = st.session_state.kit_boolean
st.session_state.kit_location = st.session_state.kit_location
st.session_state.gender = st.session_state.gender
st.session_state.fam_sub_abuse = st.session_state.fam_sub_abuse
st.session_state.per_disord = st.session_state.per_disord
st.session_state.prev_abuse = st.session_state.prev_abuse
st.session_state.depression = st.session_state.depression
st.session_state.past_sub_abuse = st.session_state.past_sub_abuse
st.session_state.addiction = st.session_state.addiction
st.session_state.dose_time = st.session_state.dose_time

st.set_page_config(
    page_title="Welcome!",
    page_icon="👋",
    initial_sidebar_state="collapsed",
    menu_items={
    'About': "Created by Team 3 for the AI4Good 2022 Toronto Cohort. Developed by Kelly Owenya."
    }
)

header = st.container()

st.sidebar.image("https://cdn.discordapp.com/attachments/940999513160687659/988264149681332274/image.png")

with header:
    st.title("**Welcome to** dose.io.")
    st.image("https://pharmchoices.com/wp-content/uploads/2021/04/5a374dca6b5fa9.6831613015135738344398.png")
    st.subheader("We'll help you make smart and informed decisions about your use of medication, all while keeping you safe.")
    if st.button("Get started"):
        st.info("Click on the sidebar in the top left to get started!")
