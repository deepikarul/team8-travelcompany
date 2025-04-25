import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.header('Flights Data')
st.write(f"### Hi, {st.session_state['first_name']}.")

flights = requests.get('http://api:4000/').json()

try:
    st.dataframe(flights)
except:
    st.write("Could not connect to database to get flights")

#"""
#Simply retrieving data from a REST api running in a separate Docker Container.

#If the container isn't running, this will be very unhappy.  But the Streamlit app 
#should not totally die. 
#"""
#data = {} 
#try:
# data = requests.get('http://api:4000/data').json()
#except:
#  st.write("**Important**: Could not connect to sample api, so using dummy data.")
#  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}
