import streamlit as st
from app import generate_response

st.set_page_config(page_title="Persona-Adaptive Customer Support Agent", layout="centered")

st.title("Persona-Adaptive Customer Support Agent")

query = st.text_area("Enter customer query:")

if st.button("Submit"):
    if query.strip() != "":
        response = generate_response(query)
        st.markdown(response)
    else:
        st.warning("Please enter a query.")