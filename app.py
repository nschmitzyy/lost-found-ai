import streamlit as st

st.set_page_config(page_title="AI Lost & Found", layout="wide")

st.title("🔎 AI Lost & Found System")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Report Lost", "Report Found", "Matches"])

if page == "Report Lost":
    st.switch_page("pages/report_lost.py")

if page == "Report Found":
    st.switch_page("pages/report_found.py")

if page == "Matches":
    st.switch_page("pages/matches.py")
