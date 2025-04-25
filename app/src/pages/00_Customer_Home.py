import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Customer, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View all Flights', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Flights.py')

if st.button('Update Client Information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Client.py')

if st.button('View Flights to specific destination city',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Flights_to.py')