import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.header('Flights Data')
st.write(f"### Hi, {st.session_state['first_name']}.")

flights = requests.get('http://api:4000/flights').json()

st.dataframe(flights)
