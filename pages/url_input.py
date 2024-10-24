# import streamlit as st
# from utils.api_client import validate_url, extract_data
# import pandas as pd
# import time

# def show_url_input_page():
#     st.title("Extract Reviews")

#     url = st.text_input("Enter the URL to extract reviews:")
    
#     if st.button("Validate URL"):
#         if url:
#             response = validate_url(url)
#             if response.status_code == 200:
#                 st.success("URL is valid!")
                
#                 # Initialize session state for data and extraction status
#                 if 'data' not in st.session_state:
#                     st.session_state.data = pd.DataFrame()  # Initialize an empty DataFrame
#                 if 'fetching_data' not in st.session_state:
#                     st.session_state.fetching_data = False
#                 if 'last_fetch_time' not in st.session_state:
#                     st.session_state.last_fetch_time = 0

#                 # Button to start data extraction
#                 if st.button("Start Data Extraction"):
#                     st.session_state.fetching_data = True  # Set fetching data flag
#                     st.session_state.last_fetch_time = time.time()  # Set the last fetch time

#             else:
#                 st.error(f"Error: {response.json().get('detail')}")
#         else:
#             st.error("Please enter a URL.")

#     # If data extraction is active, fetch data every 10 seconds
#     if 'fetching_data' in st.session_state and st.session_state.fetching_data:
#         current_time = time.time()
#         # Check if 10 seconds have passed since the last fetch
#         if current_time - st.session_state.last_fetch_time >= 10:
#             # Call the extract_data function
#             data_response = extract_data(url)  # Pass the URL to the extract_data function
#             if data_response.status_code == 200:
#                 data = data_response.json()  # Assume this returns a list of dictionaries
#                 st.session_state.data = pd.DataFrame(data)  # Update the DataFrame
#                 st.session_state.last_fetch_time = current_time  # Update fetch time
#             else:
#                 st.error(f"Error fetching data: {data_response.json().get('detail')}")

#         # Display the data in a table
#         st.write("Extracted Data:")
#         st.dataframe(st.session_state.data)

#         # Automatically rerun the script
#         time.sleep(1)  # Delay for smoother reruns
#         st.experimental_rerun()

#     # Option to stop data extraction
#     if 'fetching_data' in st.session_state and st.session_state.fetching_data:
#         if st.button("Stop Data Extraction"):
#             st.session_state.fetching_data = False  # Stop fetching data

# # Example usage:
# if __name__ == "__main__":
#     show_url_input_page()

import streamlit as st
from utils.api_client import validate_url

def show_url_input_page():
    # Check if the user is logged in
    if 'login_status' not in st.session_state or not st.session_state.login_status:
        st.error("You need to log in to access this page.")
        return  # Stop further execution if not logged in

    st.title("Extract Reviews")

    url = st.text_input("Enter the URL to extract reviews:")
    
    if st.button("Validate URL"):
        if url:
            response = validate_url(url)
            if response.status_code == 200:
                st.success("URL is valid!")
                st.balloons()  # Show balloons to celebrate success
            else:
                st.error(f"Error: {response.json().get('detail')}")
        else:
            st.error("Please enter a URL.")
