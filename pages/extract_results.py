import streamlit as st
from utils.api_client import extract_data

def show_extract_results_page():
    st.title("Extracted Reviews")

    # Call the extract_data API to get results
    extract_response = extract_data()
    if extract_response.status_code == 200:
        # Assuming the response contains a list of reviews
        reviews = extract_response.json().get('data', [])
        if reviews:
            # Display results in a table
            st.write("Extracted Reviews:")
            st.dataframe(reviews)  # Use st.dataframe for better usability
        else:
            st.warning("No reviews found.")
    else:
        st.error(f"Error extracting data: {extract_response.json().get('detail')}")
