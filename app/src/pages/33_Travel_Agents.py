import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Update Phone Number:")
agent_id = st.text_input("Enter agent id:")
phone_num = st.number_input("Enter new phone number:")
data={}
data['phoneNum'] = phone_num
requests.put('https://api:4000/a/agents/{agent_id}', json=data)