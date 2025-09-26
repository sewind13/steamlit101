import streamlit as st

# --- Assign key for button with the same text
st.button("Ok")
st.button("Ok", key="btn_ok2")  # Pass key to be ID

# --- Dynamic key (When key is a dynamic value)
'''

Slider use cobine of label, min, max, value to be key.

Problem: When the id of widget compose by dynamic input then the widget will
recreated when that parameter is changed.

Fix: Store the exiting value in the session
'''

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("Set min value", 0, 50, 25)

# This slider has min_valude parameter depend on min_value widget above.
# slider_value = st.slider(label="Slider", 
#                          min_value=min_value, 
#                          max_value=100, 
#                          value=min_value)

st.session_state.slider = st.slider(label="Slider",
                                    min_value=min_value,
                                    max_value=100,
                                    value=st.session_state.slider)

# --- 
'''
Problem: Data gone when element is stop render. The state of this element also
destroyed. 

Fix: 
'''

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show input field", value=st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
    if "user_input" not in st.session_state:
        user_input = st.text_input("Enter something:")
    else:
        user_input = st.text_input("Enter something:", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")

st.write(f"User Input: ")