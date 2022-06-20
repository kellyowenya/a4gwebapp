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
st.session_state.kit_boolean = st.session_state.kit_boolean
st.session_state.kit_location = st.session_state.kit_location
st.session_state.contact_first = st.session_state.contact_first
st.session_state.contact_phone = st.session_state.contact_phone
st.session_state.gender = st.session_state.gender
st.session_state.fam_sub_abuse = st.session_state.fam_sub_abuse
st.session_state.per_disord = st.session_state.per_disord
st.session_state.prev_abuse = st.session_state.prev_abuse
st.session_state.depression = st.session_state.depression
st.session_state.past_sub_abuse = st.session_state.past_sub_abuse
st.session_state.addiction = st.session_state.addiction
st.session_state.dose_time = st.session_state.dose_time

st.set_page_config(
   page_title="Dashboard",
   page_icon="🏠",
   layout="wide",
   initial_sidebar_state="expanded",
   menu_items={
    'About': "Created by Team 3 for the AI4Good 2022 Toronto Cohort. Developed by Kelly Owenya."
   }
)

def age(birthdate): ##credit goes to https://www.codingem.com/how-to-calculate-age-in-python/!
   today = datetime.date.today()
   one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
   year_difference = today.year - birthdate.year
   age = year_difference - one_or_zero
   return age

def suffix(d): ##credit goes to https://www.codegrepper.com/code-examples/python/how+write+a+date+with+th+and+nd++in+python
    return 'th' if 11 <= d <= 13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t): ##credit goes to https://www.codegrepper.com/code-examples/python/how+write+a+date+with+th+and+nd++in+python
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

st.sidebar.image("https://cdn.discordapp.com/attachments/940999513160687659/988264149681332274/image.png")

if len(st.session_state.first) == 0:
   st.title("Who are you?")
   st.subheader("Fill out the \"My Info\" page so we can customize your dashboard.")
else:
   st.title("How are you doing, " + st.session_state.first + "?")
   st.header(custom_strftime("Today is %A, %B {S}.", datetime.date.today()))
   
   st.image("https://jooinn.com/images/bright-sky-with-clouds.jpg")

   risk_level = 0

   if "Alcohol" in st.session_state.past_sub_abuse:
      risk_level += 3
   if "Illegal drugs" in st.session_state.past_sub_abuse:
      risk_level += 4
   if "Prescription drugs" in st.session_state.past_sub_abuse:
      risk_level += 5
   if age(st.session_state.dob) >= 16 and age(st.session_state.dob) <= 45:
      risk_level += 1
   if st.session_state.per_disord == "Yes":
      risk_level += 2
   if st.session_state.depression == "Yes":
      risk_level += 1

   if st.session_state.gender == "Male":
      if "Alcohol" in st.session_state.fam_sub_abuse:
         risk_level += 3

      if "Illegal drugs" in st.session_state.fam_sub_abuse:
         risk_level += 3

      if "Prescription drugs" in st.session_state.fam_sub_abuse:
         risk_level += 4

   elif st.session_state.gender == "Female":
      if "Alcohol" in st.session_state.fam_sub_abuse:
         risk_level += 1

      if "Illegal drugs" in st.session_state.fam_sub_abuse:
         risk_level += 2

      if "Prescription drugs" in st.session_state.fam_sub_abuse:
         risk_level += 4

      if st.session_state.prev_abuse == "Yes":
         risk_level += 3
   
   if risk_level <= 3:
      st.success("Your risk level is **Low**. *You don't seem likely to develop an opioid addiction, congratulations! Always be careful, though.*")
   elif risk_level >= 4 and risk_level <= 7:
      st.warning("Your risk level is **Moderate**. *You may develop an opioid addiction, so be on alert. Thankfully, we're watching out for you as well.*")
   else:
      st.error("Your risk level is **High**. *You're very likely to develop an opioid addiction. Let's work together to make sure that that doesn't happen.*")   

   col1, col2, col3, col4 = st.columns(4)
   col1.metric("Time until next dose", "6 hours", "09:00AM", delta_color="off")
   col2.metric("Current streak", "24 days", "+2 days more!")
   col3.metric("Intake", "3x daily", "-2 is recommended.")
   col4.metric("Last updated", "2:38pm", "+3 hours ago.")
   st.caption("*These are sample values.*")