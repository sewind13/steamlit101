import streamlit as st
import time

# --- Chche data ---
'''
cache_data is used for immutable data.
'''
@st.cache_data(ttl=60) # Cache this data for 60 seconds
def fetch_data():
    time.sleep(3)   # Simulate a slow data
    return {"data": "This is cached data!"}


st.write("Fetching data...")
data = fetch_data()
st.write(data)

# --- Cache resoruce ---
'''
We will share this resourec to everybody who hit by caching so one user modify 
data and it aan effect to another user.
'''
file_path = "example.txt"

@st.cache_resource
def get_file_handler():
    file = open(file_path, "a+")
    return file

# Use the cached file handelr
file_handler = get_file_handler()

# Write to the file using the cached handler
if st.button("Write to File"):
    file_handler.write("New line of text\n")
    file_handler.flush()
    st.success("Wrote a new line to the file!")

# Read and display the file contents
if st.button("Read File"):
    file_handler.seek(0)    # Move to begining of the file.
    content = file_handler.read()
    st.text(content)

# Always maek sure to close the file whne done (Useful for resource clenaup)
st.button("Close File", on_click=file_handler.close)
