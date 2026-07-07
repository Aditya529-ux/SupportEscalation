import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="SupportEscalation",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.title("🤖 SupportEscalation")

    st.divider()

    st.markdown("### Navigation")

    st.button("🏠 Home")
    st.button("💬 Chat")
    st.button("📊 Analytics")
    st.button("⚙️ Settings")

    st.divider()

    st.caption("Version 1.0")

# --------------------------------------------------
# Main Page
# --------------------------------------------------
st.title("🤖 AI Customer Support")

st.write("Welcome to the SupportEscalation System.")

st.info("Ask your question below.")

st.divider()

user_message = st.chat_input("Type your message...")

if user_message:
    st.chat_message("user").write(user_message)

    st.chat_message("assistant").write(
        "Thank you! AI integration starts in the coming days."
    )
