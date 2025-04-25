import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Remove a Client")

client_id = st.text_input("Enter the id of the client to be removed from the database:")
requests.delete('https://api:4000/clients/<int:client_id>', client_id)