import streamlit as st
import requests

# FastAPI backend URL
backend_url = "http://127.0.0.1:8000"

# Streamlit title
st.title("Streamlit FastAPI Interaction")

# Section 1: Interacting with the Root Endpoint
st.header("Root Endpoint")
if st.button("Get Message from FastAPI"):
    response = requests.get(f"{backend_url}/")
    if response.status_code == 200:
        st.success(f"Response: {response.json()['message']}")
    else:
        st.error("Failed to get response from FastAPI")

# Section 2: Interacting with the Dynamic Item Endpoint
st.header("Item Endpoint")
item_id = st.number_input("Enter Item ID", min_value=1, max_value=100, step=1)
query_param = st.text_input("Enter Query (optional)")

if st.button("Get Item Info"):
    # Make a request to the FastAPI endpoint
    response = requests.get(f"{backend_url}/items/{item_id}?q={query_param}")
    if response.status_code == 200:
        data = response.json()
        st.success(f"Item ID: {data['item_id']}, Query: {data['query']}")
    else:
        st.error("Failed to get response from FastAPI")
