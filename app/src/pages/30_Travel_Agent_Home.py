import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"Welcome Travel Agent, {st.session_state['first_name']}.")

if st.button('Remove a client', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/31_Clients.py')

if st.button('View Flights', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/32_Flights.py')

if st.button('Update Travel Agent Information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_Travel_Agents.py')