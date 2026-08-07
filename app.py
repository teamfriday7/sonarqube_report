import streamlit as st
import pandas as pd
import requests
from auth import check_login
from database import get_users
from utils import calculate_score


PASSWORD="admin123"

API_URL="http://localhost:5000"


st.set_page_config(
    page_title="Admin Dashboard"
)


def show_dashboard():

    st.title("User Dashboard")

    users=get_users()

    df=pd.DataFrame(users)

    st.table(df)


    for user in users:

        score=calculate_score(user[1])

        st.write(
            "User:",
            user[1],
            "Score:",
            score
        )


def login_page():

    st.title("Login")


    username=st.text_input(
        "Username"
    )

    password=st.text_input(
        "Password",
        type="password"
    )


    if st.button("Login"):

        if check_login(username,password)==True:

            st.session_state.logged=True

            st.success(
                "Login successful"
            )

        else:

            st.error(
                "Invalid login"
            )


if "logged" not in st.session_state:

    st.session_state.logged=False



if st.session_state.logged:

    show_dashboard()

else:

    login_page()