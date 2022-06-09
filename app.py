#hello!
# print("Hello world!")
import streamlit as st
import pandas as pd
import numpy as np
import os
import keyboard
import threading
import time

st.set_page_config(
    page_title="Welcome!",
    page_icon="👋",
)

header = st.container()

with header:
    st.title("Welcome to [App Name].")
    st.image("https://pharmchoices.com/wp-content/uploads/2021/04/5a374dca6b5fa9.6831613015135738344398.png")
    st.subheader("We'll help you make smart and informed decisions about your use of medication, all while keeping you safe.")
    #wait time to close page and open a new one.
    wait_second = 3.8

    #thread for closing page
    def threadFunc():
        time.sleep(wait_second)
        keyboard.press_and_release('ctrl+w')
   

    if st.button("Get started"):
        th = threading.Thread(target=threadFunc)
        th.start("http://localhost:8501/My_Info")
        #address of streamlit page that you want to open after clicking button
        os.system('D:')
        os.system('cd python\Scripts')
        os.system(r"streamlit run D:\ui\login.py")
        th.join()
