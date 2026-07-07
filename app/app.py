import streamlit as st

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="SupportEscalation",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("🤖 SupportEscalation")

    st.divider()

    st.button("🏠 Home")

    st.button("💬 Chat")

    st.button("📊 Analytics")

    st.button("⚙️ Settings")

# ---------------------------------------------------
# Main Page
# ---------------------------------------------------

st.title("🤖 AI Customer Support")

st.write("Welcome to SupportEscalation.")

st.divider()

# ---------------------------------------------------
# Display Old Messages
# ---------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------------------------------------------
# User Input
# ---------------------------------------------------

user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "Thank you! AI integration starts soon."
        }
    )

    st.rerun()
