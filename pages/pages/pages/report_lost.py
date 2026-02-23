import streamlit as st
from firebase_config import db
from datetime import datetime

st.title("Report Lost Item")

description = st.text_area("Describe the lost item")
location = st.text_input("Location")
date_lost = st.date_input("Date Lost")

if st.button("Submit"):
    if len(description) < 5:
        st.error("Description must be at least 5 characters.")
    elif not location:
        st.error("Location is required.")
    else:
        db.collection("lost_items").add({
            "description": description,
            "location": location,
            "date_lost": str(date_lost),
            "status": "open",
            "created_at": datetime.utcnow()
        })
        st.success("Lost item reported successfully!")
