import streamlit as st
import os

#--- Basics ---

# st.write: Display text in the Streamlit app
st.write("Hello, Streamlit! 12345")

# Everything automatically shows up in the app
3+4

# You can use Python's conditional expressions
"Hello, World!" if False else "Goodbye, World!"

# Anytime something must be updated on the screen, Streamlit reruns the script 
# from top to bottom.
ok_button = st.button("OK")
print(ok_button)

cancel_button = st.button("Cancel")
print(cancel_button)
