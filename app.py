mport json
from pil import image
import streamlit as st
image = image.open(image app.webp)


st.set_page_config(page_title="mywebpage",page_icon=":boat:",layout="wide")



#-- HEADER SECTION--#
with st.container():
    st.subheader("Hello, we are Rory, Toby, Rosa and Ciara :wave:")
    st.title("This is our intro to programming group project")
    st.write("[Learn more >](https://pyhtonandvba.com)","click here")

with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.subheader("What we will cover:")
        st.write("Morgage/loan calculator with a currency exchange option. ")
    with right_column:
        st.image(image)
