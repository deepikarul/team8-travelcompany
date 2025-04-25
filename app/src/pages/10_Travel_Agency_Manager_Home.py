import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Travel Agency Manager, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Flights', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Flights.py')

if st.button('View Clients of Travel Agents', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Travel_Agents.py')

if st.button("View and Add Travel Packages",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Travel_Packages.py')