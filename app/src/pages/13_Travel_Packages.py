import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()
add_logo("assets/logo.png", height=400)

st.write(f"### Hi, {st.session_state['first_name']}.")

st.write("All Travel Packages: ")
packages = requests.get('http://api:4000/packages').json()

st.write("Add a package here:")

with st.form("Create a new travel package"):
    package_ID = st.number_input("Input new package's ID:")
    name = st.text_input("Input name of new package:")
    destination = st.text_input("Input the destination of the package:")
    total_price = st.number_input("Input the total price of the package:")

    submitted = st.form.submit.button("Submit")

    if submitted:
        data = {}
        data['packageID'] = package_ID
        data['name'] = name
        data['destination'] = destination
        data['totalPrice'] = total_price
        st.write("Response submitted. Contents of Submission:")
        st.write(data)

        requests.post('https://api:4000/packages', json=data)