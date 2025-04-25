# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/40_About.py", label="About", icon="🧠")


#### ------------------------ Examples for Role of customer ------------------------
def CustomerHomeNav():
    st.sidebar.page_link(
        "pages/00_Customer_Home.py", label="Customer Home", icon="👤"
    )


def Flights01Nav():
    st.sidebar.page_link(
        "pages/01_Flights.py", label="Flights", icon="🏦"
    )


def Clients02Nav():
    st.sidebar.page_link("pages/02_Client.py", label="Client", icon="🗺️")

def d():
    st.sidebar.page_link("pages/03_.py", lable="")


## ------------------------ Examples for Role of travel agency manager ------------------------
def TravelAgencyManagerNav():
    st.sidebar.page_link(
        "pages/10_Travel_Agency_Manager_Home.py", label="Travel Agency Manager", icon="🛜"
        )


def Flights11Nav():
    st.sidebar.page_link(
        "pages/11_Prediction.py", label="Flights", icon="📈"
    )


def TravelAgents12Nav():
    st.sidebar.page_link(
        "pages/12_Travel_Agents.py", label="Travel Agents", icon="🌺"
    )

def TravelPackages13Nav():
    st.sidebar.page_link(
        "pages/13_Travel_Packages.py", label="Travel Packages", icon="🌺"
    )


#### ------------------------ Assistant Role ------------------------
def AssistantNav():
    st.sidebar.page_link("pages/20_Assistant_Home.py", label="Assistant", icon="🖥️")
    st.sidebar.page_link(
        "pages/21_Client.py", label="Client", icon="🏢"
    )
    st.sidebar.page_link("pages/22_Flights.py", label="Flights")
    st.sidebar.page_link("pages/23_.py", label="")


#### ------------------------ Travel Agent Role ------------------------
def TravelAgentNav():
    st.sidebar.page_link("pages/30_Travel_Agent_Home.py", label="Travel Agent", icon="🖥️")
    st.sidebar.page_link(
        "pages/31_Clients.py", label="Clients", icon="🏢"
    )
    st.sidebar.page_link("pages/32_Flights.py", label="Flights")
    st.sidebar.page_link("pages/33_Travel_Agents.py", label="")


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # If the user is a customer
        if st.session_state["role"] == "customer":
            CustomerHomeNav()
            Flights01Nav()
            Clients02Nav()
            d()

        # If the user is a travel agency manager
        if st.session_state["role"] == "travel_agency_manager":
            TravelAgencyManagerNav()
            Flights11Nav()
            TravelAgents12Nav()
            TravelPackages13Nav()

        # If the user is an assistant
        if st.session_state["role"] == "assistant":
            AssistantNav()

        # If the user is a travel agent
        if st.session_state["role"] == "travel_agent":
            TravelAgentNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
