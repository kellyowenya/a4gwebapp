import streamlit as st
import datetime

st.session_state.active_page = st.session_state.active_page
st.session_state.first = st.session_state.first
st.session_state.last = st.session_state.last
st.session_state.dob = st.session_state.dob
st.session_state.blood = st.session_state.blood
st.session_state.height = st.session_state.height
st.session_state.weight = st.session_state.weight
st.session_state.prev_overdose = st.session_state.prev_overdose
st.session_state.prev_hosp = st.session_state.prev_hosp
st.session_state.current_drugs = st.session_state.current_drugs
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
    page_title="My Info",
    page_icon="🧑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    'About': "Created by Team 3 for the AI4Good 2022 Toronto Cohort. Developed by Kelly Owenya."
    }
)

st.sidebar.image("https://cdn.discordapp.com/attachments/940999513160687659/988264149681332274/image.png")

st.header("Tell us a bit about yourself.")
st.caption("Don't worry, you can change this information at any time, and everything will adjust accordingly!")
st.markdown("**Remember to hit the \"Submit\" button when you're done**.")

def form_callback():
    # st.write(st.session_state.first)
    st.balloons()
    st.session_state.first = st.session_state.first
    st.session_state.last = st.session_state.last
    st.session_state.dob = st.session_state.dob
    st.session_state.blood = st.session_state.blood
    st.session_state.height = st.session_state.height
    st.session_state.weight = st.session_state.weight
    st.session_state.current_drugs = st.session_state.current_drugs
    st.session_state.prev_overdose = st.session_state.prev_overdose
    st.session_state.prev_hosp = st.session_state.prev_hosp
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


with st.form("user_info"):
    
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("First Name", max_chars=20, key="first")
    with col2:
        st.text_input("Last Name", max_chars=20, key="last")
    
    gender = st.radio("What's your gender?", ("Male", "Female"), help="If you identify as a different gender than the one assigned to you at birth, please put your birth gender here.", key="gender", horizontal=True)
    st.date_input("When's your birthday?", min_value=datetime.date(1910, 1, 1), key="dob")
    st.slider('How tall are you?', 100, 250, 175, format="%d cm", key="height")
    st.slider('How much do you weigh?', 35, 150, 75, format="%d kg", key="weight")
    st.selectbox("What's your blood type?", ['Unknown', 'A+', "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], key="blood")

    st.header("We may need some additional background information...")
    st.info("In order to properly assess your opioid addiction risk level, some personal details and factors may be considered, which may be potentially triggering. We ask for these details so we can ensure our analysis is as correct as possible, resulting in the most accurate experience for you.")
    
    with st.expander("Sensitive information"):
        st.multiselect('Does anyone in your family have a history of substance abuse with any of these drugs?', ['Alcohol', 'Illegal drugs', 'Prescription drugs'], key="fam_sub_abuse")
        colu1, colu2, colu3 = st.columns(3)
        with colu1:
            st.radio("Have you been diagnosed with ADD, OCD, bipolar disorder, or schizophrenia?", ("Yes", "No"), key="per_disord")
        with colu2:
            st.radio("Are you currently suffering from depression?", ("Yes", "No"), key="depression")
        with colu3:
            st.radio("Do you have a history of preadolescent sexual abuse?", ("Yes", "No"), key="prev_abuse")

    st.header("Now, about your medicine intake.")
    st.multiselect("What opioid medications or drugs are you currently taking?",
    ["Codeine", "Oxycodone", "Morphine", "Hydromorphone", "Fentanyl", "Heroin", "Methadone", "Buprenorphine"], help="You can select more than one off of this list.", key="current_drugs")
    st.multiselect('Do you have a history of substance abuse with any of these drugs?', ['Alcohol', 'Illegal drugs', 'Prescription drugs'], key="past_sub_abuse")
    column1, column2, column3 = st.columns(3)
    with column1:
        st.radio("Are you currently in treatment for any addiction?", ("Yes", "No"), key="addiction")
    with column2:
        st.radio("Have you previously overdosed on any drug?", ("Yes", "No"), key="prev_overdose")
    with column3:
        st.radio("Have you been hospitalized in the past 6 months?", ("Yes", "No"), key="prev_hosp")

    st.time_input("At what time do you usually prefer to take your prescription medication?", datetime.time(9, 00), key="dose_time")
    
    st.radio("Do you have a naloxone kit in case of an overdose emergency in your home?", ("Yes", "No"), index=1, horizontal=True)
    st.text_input("If so, where is it located?", help="Describe the location in such a way that others will be able to find it in case of an emergency.", key="kit_location", placeholder="Example: \"In the bathroom at the top of the stairs, green box...\"")

    st.header("And, finally...who's your emergency contact?")
    colum1, colum2 = st.columns(2)
    with colum1:
        contact_name = st.text_input("Contact's full name", key="contact_first")
    with colum2:
        contact_phone = st.text_input("Contact's phone number", key="contact_phone")
    
    st.write("That's all we need from you right now!")
    st.markdown("*Head over to your customized Dashboard to see our analysis at work.*")
    st.form_submit_button("Submit!", on_click=form_callback)


    