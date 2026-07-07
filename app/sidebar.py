import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🤖 SupportEscalation")

        st.divider()

        st.button("🏠 Home")

        st.button("💬 Chat")

        st.button("📊 Analytics")

        st.button("⚙️ Settings")

        st.divider()

        st.caption("Version 1.0")
