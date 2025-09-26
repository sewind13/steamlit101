import streamlit as st

'''
Session State: It is something that we can use to store value within the same 
user session. It is useful when we want to keep track of certain values or 
states
'''

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter after increment: {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")
