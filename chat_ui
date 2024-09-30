import os
import streamlit as st
from groq import Groq
from datetime import datetime

# Set up the Streamlit page
st.title("AI Chat Assistant")

# Initialize Groq client with API key from environment variable
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY environment variable is not set. Please set it and restart the app.")
    st.stop()

# Initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for chat history
with st.sidebar:
    st.subheader("Chat History")
    if st.session_state.chat_history:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.text(f"You: {message['content']}")
            elif message["role"] == "assistant":
                st.text(f"Assistant: {message['content']}")

# Input text box for user query
user_input = st.text_input("Enter your message:", key="user_input")

# Handle user input
if user_input:
    # Append user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Here you would typically call your AI assistant to get a response
    # For demonstration, we'll just echo the user's message
    assistant_response = f"Echo: {user_input}"
    
    # Append assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    
    # Clear the input box
    st.session_state.user_input = ""

# Display the chat history in the main area
st.subheader("Chat")
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.text(f"You: {message['content']}")
    elif message["role"] == "assistant":
        st.text(f"Assistant: {message['content']}")