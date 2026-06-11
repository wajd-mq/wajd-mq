import os

import requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")

st.title("🌤 Weather Dashboard")

city = st.text_input("Enter City", "Muscat")

if st.button("Get Weather"):
    try:
        response = requests.get(f"{BACKEND_URL}/weather", params={"city": city}, timeout=60)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            st.error(f"Error: {data['error']}")
        else:
            st.subheader("Weather Result")
            st.write(data)

    except Exception as e:
        st.error(f"Error: {e}")