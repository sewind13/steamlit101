import streamlit as st

# --- Sidebar ---
st.sidebar.title("This is sidebar")
st.sidebar.write("This is a sidebar")
sidebar_input = st.sidebar.text_input("Sidebar input")

# --- Tabs layout ---
tab1, tab2, tab3 = st.tabs(["Daily Dashboard", "Monthly Dashboard", "Tab 3"])

with tab1:
    st.header("Content for Tab 1")
    st.write("This is the content of Tab 1")

with tab2:
    st.header("Content for Tab 2")
    st.write("This is the content of Tab 2")

with tab3:
    st.header("Content for Tab 3")
    st.write("This is the content of Tab 3")

# --- Columns layout ---
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("This is the content of Column 1")

with col2:
    st.header("Column 2")
    st.write("This is the content of Column 2")

with col3:
    st.header("Column 3")
    st.write("This is the content of Column 3")

# --- Container layout ---
with st.container(border=True):
    st.header("Container Section")
    st.write("This is inside a container")

# --- Empty Placeholder ---
placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful for dynamic content.")

if st.button("Update Placeholder"):
    placeholder.write("The content of this placeholder has been updated.")

# --- Exander ---
with st.expander("Expand for more details"):
    st.write("This is additional information that is hidden by default.")
    st.write("You can use expanders to keep your interface cleaner.")

# Popover (Tooltip)
st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooltip or popover on hover.")

# --- Sidebar ---
if sidebar_input:
    st.write(f"You entered in the sidebar: {sidebar_input}")