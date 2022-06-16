import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(
    page_title="Emergencies",
    page_icon="🚑",
)

emergency_page = st.container()

with emergency_page:
    st.header("Overdosed and need help?")
    st.image("https://www.tuningblog.eu/wp-content/uploads/2019/12/Sondersignalanlagen-Martinshorn-Blaulicht-e1576214416785.jpg")
    st.subheader("*You're not alone*. We have **resources** for you.")
    overdoses = st.multiselect("What medication(s) did you overdose from?", ["Codeine", "Oxycodone", "Morphine", "Hydromorphone", "Fentanyl", "Heroin", "Methadone", "Buprenorphine"], help="You may select multiple if applicable.")
    overdose_time = st.time_input("At what time did you take the drugs?", datetime.time())
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
    
    with st.expander("working on smth ~ kelly"):
        st.write("If user indicates that they have a naloxone kit and the location of it in their house, it'll show up here so the user or their trusted person knows where to get it. can't finish this until i figure out global variables.")
    st.write("If you don't have a naloxone kit where you are right now, here's a map that shows your closest naloxone kit location. If possible/close, call a friend or family member to get one for you while the ambulance arrives.")
    st.map()
    nal_status = st.radio("Were you able to successfully administer naloxone?", ("Yes", "No"), index=1)

    st.subheader("Overdose Summary")
    st.info("This is where all the details you inputted regarding your overdose are summarized. We'll be forwarding a copy of this to your nearest opioid treatment centre and your emergency contact, if applicable. **Feel free to copy and paste, and share it with others as you see fit.**")
    with st.expander("Your Overdose Summary"):
        st.write("**Patient Name:** Firstname Lastname (working on global variables ~ Kelly)")
        st.write("**Drugs Overdosed On:**", overdoses)
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
        
        if nal_status == "Yes":
            st.write("**Naloxone Administered:** Yes")

        else:
            st.write("**Naloxone Administered:** No")