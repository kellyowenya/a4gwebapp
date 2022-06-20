import streamlit as st
import datetime

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
    page_title="Emergencies",
    page_icon="🚑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    'About': "Created by Team 3 for the AI4Good 2022 Toronto Cohort. Developed by Kelly Owenya."
    }
)

st.sidebar.image("https://cdn.discordapp.com/attachments/940999513160687659/988264149681332274/image.png")

def age(birthdate): ##credit goes to https://www.codingem.com/how-to-calculate-age-in-python/!
    today = datetime.date.today()
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
    year_difference = today.year - birthdate.year
    age = year_difference - one_or_zero
    return age

emergency_page = st.container()

with emergency_page:
    st.header("Overdosed and need help?")
    st.image("https://www.tuningblog.eu/wp-content/uploads/2019/12/Sondersignalanlagen-Martinshorn-Blaulicht-e1576214416785.jpg")
    st.subheader("*You're not alone*. We have **resources** for you.")
    if st.button("I need help, immediately."):
        st.write("First, we're forwarding important medical emergency data straight to your nearest opioid treatment center.")
        with st.expander("Your Initial (Immediate) Overdose Summary"):
            st.write("**Patient Name:** " + st.session_state.first + " " + st.session_state.last)
            st.write("**Age:**", str(age(st.session_state.dob)))
            st.write("**Blood Type:**", st.session_state.blood)
            st.write("**Height:** " + str(st.session_state.height) + " cm")
            st.write("**Weight:**", str(st.session_state.weight) + " kg")
            if st.session_state.current_drugs == []:
                st.write("**Drugs Currently Taking:** None")
            else:
                st.write("**Drugs Currently Taking:**", ", ".join(st.session_state.current_drugs))
            st.write("**Previously overdosed?:**", st.session_state.prev_overdose)
            st.write("**Hospitalized in past 6 months?:**", st.session_state.prev_hosp)
            if st.session_state.contact_first == "" or st.session_state.contact_phone == "":
                st.write("**Emergency Contact:** None provided")
            else:
                st.write("***Emergency Contact:***")
                st.write(st.session_state.contact_first + ", phone at:  " + st.session_state.contact_phone)

    overdoses = st.multiselect("What medication(s) did you overdose from?", ["Codeine", "Oxycodone", "Morphine", "Hydromorphone", "Fentanyl", "Heroin", "Methadone", "Buprenorphine"], help="You may select multiple if applicable.")
    overdose_time = st.time_input("At what time did you take the drugs?")
    st.error("As with all medical emergencies, calling your local emergency number should be your first priority. *No matter where you are, you deserve to know where to seek help.*")
    
    with st.expander("List of all major emergency ambulance numbers"):
        st.markdown("**North America:** 911\n")
        st.markdown("**Europe:** 112\n")
        st.markdown("**Australia:** 000\n")
        st.markdown("**China:** 120\n")
        st.markdown("**Cuba:** 104\n")
        st.markdown("**Hong Kong:** 999\n")
        st.markdown("**India:** 112\n")
        st.markdown("**Japan:** 119\n")
        st.markdown("**New Zealand:** 111\n")
        st.markdown("Click here for a __full comprehensive list__ of every country: https://worldpopulationreview.com/country-rankings/911-by-country")
    
    st.subheader("Symptoms")
    st.info("If you don't feel well enough to answer the questions accurately, please alert a trusted person to fill these out for you.")
    
    column1, column2, column3 = st.columns(3)
    with column1:
        face = st.radio("Is your face extremely pale and/or feels clammy to the touch?", ("Yes", "No"), index=1)
        body = st.radio("Does your body feel limp?", ("Yes", "No"), index=1)
    with column2:
        blurple = st.radio("Do your fingernails or lips have a purple or blue color?", ("Yes", "No"), index=1)
        drowsy = st.radio("Are you feeling drowsy and slow to speak?", ("Yes", "No"), index=1)
    with column3:
        nausea = st.radio("Have you recently vomited or are you feeling nauseous to the point of vomiting?", ("Yes", "No"), index=1)
        slowing = st.radio("Is your heartbeat or pulse slowing?", ("Yes", "No"), index=1)
    st.markdown("Thank you for your responses. We're forwarding this information to your emergency contact (if provided) and your local emergency centre so you can get efficient and fast treatment.")
    
    st.subheader("Naloxone Kits")
    st.info("Naloxone is the most common drug used to **reverse the effects of an opioid overdose temporarily**. Naloxone is **non-addictive**, and can be administered *to and by anyone, without any special training*. It can be injected or sprayed. The effects are *temporary* to provide time for medical personnel to arrive.")
    
    if st.session_state.kit_location != "":
        st.success("You're in luck! **There's a naloxone kit that you have (or the user of the app has) previously provided the location of!**")
        st.markdown("**Instructions on its location:** " + st.session_state.kit_location)
    else:
        st.error("Doesn't look like a known naloxone kit location was provided by you in the \"My Info\" page. **If you haven't already, call 911 as soon as you can.**")
    nal_status = st.radio("Were you able to successfully administer naloxone?", ["Yes", "No"], index=1)

    st.subheader("Overdose Summary")
    st.info("This is where all the details you inputted regarding your overdose are summarized. We'll be forwarding a copy of this to your nearest opioid treatment centre and your emergency contact, if applicable. **Feel free to copy and paste, and share it with others as you see fit.**")
    with st.expander("Your Complete Overdose Summary"):
        st.write("**Patient Name:** " + st.session_state.first + " " + st.session_state.last)
        st.write("**Age:**", str(age(st.session_state.dob)))
        st.write("**Blood Type:**", st.session_state.blood)
        st.write("**Height:** " + str(st.session_state.height) + " cm")
        st.write("**Weight:**", str(st.session_state.weight) + " kg")
        if st.session_state.current_drugs == []:
            st.write("**Drugs Currently Taking:** None")
        else:
            st.write("**Drugs Currently Taking:**", ", ".join(st.session_state.current_drugs))
        st.write("**Previously overdosed?:**", st.session_state.prev_overdose)
        st.write("**Hospitalized in past 6 months?:**", st.session_state.prev_hosp)
        if st.session_state.contact_first == "" or st.session_state.contact_phone == "":
            st.write("**Emergency Contact:** None provided")
        else:
            st.write("***Emergency Contact:***")
            st.write(st.session_state.contact_first + ", phone at:  " + st.session_state.contact_phone)
        st.write("--- **Overdose Details** ---")
        st.write("**Drugs Overdosed On:**", ", ".join(overdoses))
        st.write("**Time of Overdose:**", overdose_time)
        st.write("**List of Symptoms:**")
        if face == "Yes":
            st.write("- Person's face is extremely pale and/or feels clammy to the touch")
        if body == "Yes":
            st.write("- Person's body feels limp")
        if blurple == "Yes":
            st.write("- Person's fingernails or lips have a purple or blue color")
        if drowsy == "Yes":
            st.write("- Person feeling drowsy and slow to speak")
        if nausea == "Yes":
            st.write("- Person has vomited or feels nauseous to the point of vomiting")
        if slowing == "Yes":
            st.write("- Person's heartbeat or pulse is slowing")
        st.write(" ")
        
        if nal_status == "Yes":
            st.write("**Naloxone Administered:** Yes")

        else:
            st.write("**Naloxone Administered:** No")
    st.write("Thank you for filling this out. The earlier the proper people have this information, the better the situation can be handled. We're wishing you all the best right now, and we hope you make a speedy recovery.")
    st.write("**Take care.**")