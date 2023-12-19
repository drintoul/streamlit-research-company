import streamlit as st
import requests


text_search = st.text_input("Search videos by title or speaker", value="")

st.write(text_search)
