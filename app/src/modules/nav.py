# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


#### ------------------------ Examples for Student ------------------------
def Student_Profile():
    st.sidebar.page_link(
        "pages/31_Student_Profile.py", label="Student Profile", icon="👤"
    )


# def WorldBankVizNav():
#     st.sidebar.page_link(
#         "pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon="🏦"
#     )


# def MapDemoNav():
#     st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon="🗺️")

#### ------------------------ Examples for Alumn ------------------------
def Alumn_Profile():
    st.sidebar.page_link(
        "pages/33_Alumn_Profile.py", label="Alumn Profile", icon="👤"
    )


# def WorldBankVizNav():
#     st.sidebar.page_link(
#         "pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon="🏦"
#     )


# def MapDemoNav():
#     st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon="🗺️")


## ------------------------ Examples Company employee ------------------------
def Company():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon="🛜")


def PostJob():
    st.sidebar.page_link(
        "pages/11_Post_Job.py", label="PostJob", icon="📈"
    )


# def ClassificationNav():
#     st.sidebar.page_link(
#         "pages/13_Classification.py", label="Classification Demo", icon="🌺"
#     )


#### ------------------------ Advisor ------------------------
def AdvisorHome():
    st.sidebar.page_link(
        "pages/Advisor_Home.py", label="Advisor Home", icon="🏠"
    )
def AdvisorProfile():
    st.sidebar.page_link(
        "pages/Advisor_Profile.py", label="Advisor Profile", icon="👤"
    )

#### ------------------------ System Admin Role ------------------------
def Admin_Profile():
    st.sidebar.page_link(
        "pages/42_Admin_Profile.py", label="Student Profile", icon="👤"
    )
def See_Tickets():
    st.sidebar.page_link(
        "pages/43_See_Tickets.py", label="See Tickets", icon="⏳"
    )
def See_All_Users():
    st.sidebar.page_link(
        "pages/44_See_All_Users.py", label="See All Users", icon="🧑‍💻"
    )



# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/CC_Logo.png", width=250)
    

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.write('\n\n')
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()
    
    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:
        
        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state["role"] == "student":
            st.write('\n\n')
            Student_Profile()
            # WorldBankVizNav()
            # MapDemoNav()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state["role"] == "company":
            st.write('\n\n')
            PostJob()
            # ApiTestNav()
            # ClassificationNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "alumn":
            st.write('\n\n')
            Alumn_Profile()

         # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            st.write('\n\n')
            Admin_Profile()
            See_Tickets()
            See_All_Users()

        # If the user is an advisor, give them access to the advisor pages 
        if st.session_state["role"] == "advisor":
            st.write('\n\n')
            AdvisorProfile()
            AdvisorHome()


    # Always show the About page at the bottom of the list of links
    AboutPageNav()
    
    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
