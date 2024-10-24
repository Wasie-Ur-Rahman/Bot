import streamlit as st
from utils.api_client import login

def show_login_page():
    st.title("Login")

    username = st.text_input("User Name")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = login(username, password)
        if response.status_code == 200:
            st.success(response.json().get('message'))
            st.session_state.login_status = True  # Update login status
            st.session_state.username = username  # Store username if needed

            # Redirect to the URL input page by changing the session state
            st.session_state.page = "Extract Reviews"  # Set the page to 'Extract Reviews'

        else:
            st.error(f"Error: {response.json().get('detail')}")

    # Display content if already logged in
    if st.session_state.login_status:
        st.write("Welcome back! Please proceed to extract reviews.")
