import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

st.write("Update phone number:")

client_id = st.text_input("Enter client id:")
phone_num = st.number_input("Enter new phone number:")
data={}
data['phoneNum'] = phone_num
requests.put('https://api:4000/c/clients/{client_id}', json=data)