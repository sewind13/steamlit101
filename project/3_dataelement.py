import streamlit as st
import pandas as pd


st.title("Data Elements")

# --- Dataframe ---
st.subheader("Dataframe")
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})
st.dataframe(df)

# --- Editable Dataframe ---
st.subheader("Editable Dataframe")
edited_df = st.data_editor(df)

# --- Table ---
st.subheader("Table")
st.table(df)

# --- Metrics ---
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Sum of Column 1", value=df['Column 1'].sum(), delta=1)

# --- JSON ---
st.subheader("JSON")
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
st.json(data)

# --- Dictionay ---
st.subheader("Dictionary")
st.write("Dictionary Example:", data)

# --- Progress Bar ---  
st.subheader("Progress Bar")
import time
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1) 
