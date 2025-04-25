import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.header('Flights Data')
st.write(f"### Hi, {st.session_state['first_name']}.")

flights = requests.get('http://api:4000/f/flights').json()

st.dataframe(flights)