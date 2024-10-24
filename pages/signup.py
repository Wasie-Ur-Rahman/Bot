import streamlit as st
from utils.api_client import signup

def show_signup_page():
    st.title("Sign Up")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if password != confirm_password:
            st.error("Passwords do not match!")
        else:
            response = signup(username, email, password)
            if response.status_code == 200:
                st.success("Account created successfully! You can now log in.")
            else:
                st.error(f"Error: {response.json().get('detail')}")
