import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="DEEPSEED Chat", layout="wide", initial_sidebar_state="expanded")

# --- Quick actions and their replies ---
quick_actions = {
    "Tell me a joke": "Why don't scientists trust atoms? Because they make up everything! 😂",
    "Explain AI": "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.",
    "Help brainstorm": "Sure! Let's brainstorm some ideas together. What topic are you interested in?",
    "Writing tips": "Writing tips: Keep sentences short, use active voice, and be clear!",
    "Book recommendations": "I recommend 'Atomic Habits' by James Clear and 'Deep Work' by Cal Newport."
}

if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("🌱 DEEPSEED")
    st.caption("*one seed at a time*")

    "---"

    st.subheader("📊 Session Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Messages", len(st.session_state.messages))
    with col2:
        st.metric("Total", len(st.session_state.messages))

    st.markdown("---")

    st.subheader("🚀 Quick Actions")
    for action in quick_actions.keys():
        if st.button(action, use_container_width=True):
            # Add user message (quick action clicked)
            st.session_state.messages.append({
                "role": "user",
                "text": action,
                "time": datetime.now().strftime("%H:%M")
            })
            # Add assistant reply for that quick action
            st.session_state.messages.append({
                "role": "assistant",
                "text": quick_actions[action],
                "time": datetime.now().strftime("%H:%M")
            })

    st.markdown("---")

    st.subheader("⚙️ Controls")

# Main chat area
st.header("💬 Chat with DEEPSEED")
    

if len(st.session_state.messages) == 0:
    col1, col2, col3 = st.columns([1,5,1])
    col2.write("*Type your message below to start or choose a quick action from the sidebar.*")
    
else:
    message_box = st.container(border=True, height=400, gap="small")

    with message_box:

        for msg in st.session_state.messages:
            if msg["role"] == "user":
                col_left, col_right = st.columns([0.3, 0.7])
                with col_right:
                    with st.chat_message(msg["role"]):
                        st.write(msg["text"]) # ({msg.get('time', '')})

            elif msg["role"] == "assistant":
                col_left, col_right = st.columns([0.7, 0.3]) 
                with col_left:
                    with st.chat_message(msg["role"]):
                        st.write(msg["text"]) # ({msg.get('time', '')})

user_input = st.chat_input(placeholder="Type your message here...")

if user_input:
    time_now = datetime.now().strftime("%H:%M")
    # Append user message
    st.session_state.messages.append({
        "role": "user",
        "text": user_input,
        "time": time_now
    })

    matched_reply = None
    for action_text, reply_text in quick_actions.items():
        if action_text.lower() in user_input.lower():
            matched_reply = reply_text
            break

    with st.spinner("DEEPSEED is thinking..."):
        time.sleep(2)  # Simulate processing delay

    assistant_reply = matched_reply or " Based on your message, I can provide some insights on this."
    st.session_state.messages.append({
        "role": "assistant",
        "text": assistant_reply,
        "time": time_now
    })

if st.session_state.messages:
    var_total_messages = len(st.session_state.messages)
    session_id = st.session_state.get("session_id", "N/A")
    st.caption(f"{var_total_messages} messages in the current session  ●  Session: {session_id}")
