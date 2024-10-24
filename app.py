# import streamlit as st
# from pages.signup import show_signup_page
# from pages.login import show_login_page
# from pages.url_input import show_url_input_page
# from pages.extract_results import show_extract_results_page  # Import the new page

# def main():
#     st.sidebar.title("Navigation")
    
#     # Check login status
#     if 'login_status' not in st.session_state:
#         st.session_state.login_status = False  # Default to not logged in

#     # Sidebar navigation logic
#     if st.session_state.login_status:
#         # If logged in, show options for URL input and results
#         page = st.sidebar.radio("Go to", ("Extract Reviews", "Extract Results"))
#         if st.sidebar.button("Logout"):  # Always visible logout button
#             st.session_state.login_status = False  # Set login status to False
#             st.session_state.page = "Login"  # Redirect to Login page
#     else:
#         # If not logged in, only show Login and Sign Up options
#         page = st.sidebar.radio("Go to", ("Login", "Sign Up"))

#     # Display the selected page
#     if page == "Login":
#         show_login_page()
#     elif page == "Sign Up":
#         show_signup_page()
#     elif page == "Extract Reviews":
#         show_url_input_page()
#     elif page == "Extract Results":
#         show_extract_results_page()  # Navigate to the extract results page

# if __name__ == "__main__":
#     main()

import streamlit as st
from pages.signup import show_signup_page
from pages.login import show_login_page
from pages.url_input import show_url_input_page
from pages.extract_results import show_extract_results_page  # Import the new page
from pages.report_review import show_report_page  # Import the report page

def main():
    st.sidebar.title("Navigation")
    
    # Check login status
    if 'login_status' not in st.session_state:
        st.session_state.login_status = False  # Default to not logged in

    # Sidebar navigation logic
    if st.session_state.login_status:
        # If logged in, show options for URL input, results, and report
        page = st.sidebar.radio("Go to", ("Extract Reviews", "Extract Results", "Report Reviews"))
        if st.sidebar.button("Logout"):  # Always visible logout button
            st.session_state.login_status = False  # Set login status to False
            st.session_state.page = "Login"  # Redirect to Login page
    else:
        # If not logged in, only show Login and Sign Up options
        page = st.sidebar.radio("Go to", ("Login", "Sign Up"))

    # Display the selected page
    if page == "Login":
        show_login_page()
    elif page == "Sign Up":
        show_signup_page()
    elif page == "Extract Reviews":
        show_url_input_page()
    elif page == "Extract Results":
        show_extract_results_page()  # Navigate to the extract results page
    elif page == "Report Reviews":
        show_report_page()  # Navigate to the report page

if __name__ == "__main__":
    main()
