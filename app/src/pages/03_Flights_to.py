import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()
st.header('Flights to Specific Destination Data')
st.write(f"### Hi, {st.session_state['first_name']}.")

dest_city = st.text_input("Enter the destination to get flights going there:")
flightsTo = requests.get('https://api:4000/f/flights/to/{dest_city}').json()
st.dataframe(flightsTo)