import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"Welcome Assistant, {st.session_state['first_name']}.")

if st.button('Update Client Information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Client.py')

if st.button('View Flights', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Flights.py')

if st.button('', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_.py')