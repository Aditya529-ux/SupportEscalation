import streamlit as st

from sidebar import render_sidebar

from ui import render_main_page

from chat import (
    initialize_chat,
    display_chat,
    handle_chat
)

st.set_page_config(
    page_title="SupportEscalation",
    page_icon="🤖",
    layout="wide"
)

initialize_chat()

render_sidebar()

render_main_page()

display_chat()

handle_chat()
