import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.header('Client Data')
st.write(f"### Hi, {st.session_state['first_name']}.")

agent_ID = st.number_input("Enter agent ID:")

clients = requests.get('http://api:4000/a/agents/{agent_id}/clients').json()
st.dataframe(clients)