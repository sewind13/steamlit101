import streamlit as st

'''
Callbacks: Functions that are called when an event occurs, such as a button

Issue: When you click a button, the script is rerun from top to bottom, then it
update the UI before update the state.

Fix: Use callbacks to update the state before the script is rerun to generate 
the UI.
'''

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = dict()

# Callback to go to step 2
# We need it to update value before reloading the script
def go_to_step2(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2

def go_to_step1():
    st.session_state.step = 1

if st.session_state.step == 1:
    st.header("Step 1")
    name = st.text_input("Enter your name",
                         value=st.session_state.info.get("name", ""))

    st.button("Next", on_click=go_to_step2, args=(name,))


if st.session_state.step == 2:
    st.header("Step 2")

    st.subheader("Please review this: ")
    st.write(f"**Name**: {st.session_state.info.get('name', '')}")

    if st.button("Submit"):
        st.success("Great! Form submitted.")
        st.balloons()
        st.session_state.info = dict()
    
    st.button("Back", on_click=go_to_step1)
       
   