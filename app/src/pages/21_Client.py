import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

client_id = st.text_input("Enter the id of the client to be removed from the database:")
requests.delete('https://api:4000/clients/<int:client_id>', client_id)
