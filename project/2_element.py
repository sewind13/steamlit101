import streamlit as st
import os


#--- Elements ---
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.text("This is a text")
st.markdown("This is a markdown")
st.latex(r"E=mc^2")

code_example = """
def hello():
    print("Hello, World!")
"""
st.code(code_example, language="python")
st.divider()
st.image(os.path.join(os.getcwd(), "static", "pokestop.jpg"), 
         caption="This is an image",
         width=300)


#--- Data Elements ---
