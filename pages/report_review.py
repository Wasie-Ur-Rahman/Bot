import streamlit as st
from utils.api_client import report  # Import the report function

def show_report_page():
    st.title("Report Page")

    # Add a button to trigger the report function
    if st.button("Report Reviews"):
        # Call the report API
        report_response = report()
        
        # Check the response status
        if report_response.status_code == 200:
            st.success("Report generated successfully!")
            st.balloons()  # Show balloons
        else:
            st.error(f"Error generating report: {report_response.json().get('detail', 'Unknown error')}")

