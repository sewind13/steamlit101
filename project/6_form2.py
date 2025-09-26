import streamlit as st
from datetime import datetime

# --- Title ---
st.title("Streamlit Forms Example 2")

# --- Form data ---

form_values = {
    "name": None,
    "gender": None,
    "dob": None,
    "location": None
}

min_date = datetime(1990, 1, 1)
max_date = datetime.now()

with st.form(key='user_info_form'):
    form_values["name"] = st.text_input(label='Enter your name')
    form_values["gender"] = st.selectbox(label='Select your gender',
                                          options=['Male', 'Female', 'Other'])
    form_values["dob"] = st.date_input(label='Select your date of birth'
                                        , min_value=min_date
                                        , max_value=max_date)
    form_values["location"] = st.text_input(label='Enter your location')

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:

        # Validate all data is filled
        if not all(form_values.values()):
            st.warning("Please fill in all fields.")
        else:
            st.balloons()
            st.write("### Form Data:")
            for key, value in form_values.items():
                st.write(f"{key}: {value}")