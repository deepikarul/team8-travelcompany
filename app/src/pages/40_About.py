import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    Welcome to Explore Beyond! 
    
    We are a travel company that was created with the purpose of making it easier and more efficient to plan trips! 

    We hope these services make booking flights, hotels and activities stressfree!

    Our services also allow you to be able to work with a travel agent who will help plan the trip of your dreams!
    """
        )
