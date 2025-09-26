import streamlit as st
import pandas as pd

# --- Title ---
st.title("Streamlit Forms Example")

# Form to hold the interactive widgets
with st.form(key='sample_form'):

    # Input fields
    text_input = st.text_input(label='Enter some text')
    number_input = st.number_input(label='Enter a number',
                                    min_value=0, 
                                    max_value=100)
    text_area = st.text_area(label='Provide feedback')

    # Date and time input
    date = st.date_input(label='Select a date')
    time = st.time_input(label='Select a time')

    # Selector
    choice = st.radio(label='Choose an option',
                      options=['Option 1', 'Option 2', 'Option 3'])
    gender = st.selectbox(label='Select your gender',
                           options=['Male', 'Female', 'Other'])
    slider_value = st.slider(label='Select a range of values',
                             min_value=0, 
                             max_value=100, 
                             value=(25, 75))
    
    # Toggle and checkbox
    agree = st.checkbox(label='I agree to the terms and conditions')
    notifications = st.toggle(label='Enable notifications')



    # Submit button
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write("Text:", text_input)
        st.write("Number:", number_input)