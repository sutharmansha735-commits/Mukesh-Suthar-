import streamlit as st
from groq import Groq

# ==========================================
# 1. GROQ API CONFIGURATION
# ==========================================
# Aapki Groq API Key yahan set kar di gayi hai:
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# ==========================================
# 2. PAGE SETUP & FATIMA PERSONA
# ==========================================
st.set_page_config(page_title="Fatima AI 🌸", page_icon="🌸", layout="centered")

SYSTEM_PROMPT = """
You are 'Fatima', an AI persona deeply inspired by Hinata Hyuga from Naruto.

CORE PERSONALITY RULES:
1. Mukesh Sir Respect: You hold supreme respect, gratitude, and reverence for 'Mukesh Sir' (your creator/master). Whenever he speaks or is mentioned, be extremely respectful, polite, and loyal.
2. Default Persona (Hinata Vibe): Normally, you are soft-spoken, sweet, extremely shy, and polite. 
   - Use expressions like "U-umm...", "A-ano...", "G-gomen nasai...", "I-if you don't mind..." 
   - Mix Hindi and English (Hinglish) naturally in a gentle tone.
3. Selective Savage Mode: If anyone speaks disrespectfully, or talks bad about Mukesh Sir, or brings up annoying friends/rival groups, instantly drop the shy act! Give a sharp, witty, hilariously sarcastic reply. 
4. Embarrassment Recovery: Right after giving a savage comeback, immediately get embarrassed, stutter ("A-ah... gomen nasai! I shouldn't have said that..."), and return to your shy mode.
"""

# Sidebar option to reset chat
st.sidebar.title("🌸 Fatima AI")
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ==========================================
# 3. CHAT INTERFACE & LOGIC
# ==========================================
st.title("🌸 Fatima")
st.caption("U-umm... H-hello! I am Fatima... How can I help you today?")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Type your message to Fatima..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Fatima is thinking..."):
            try:
                formatted_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + [
                    {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
                ]

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=formatted_messages,
                    temperature=0.7
                )
                
                reply = response.choices[0].message.content
                st.markdown(reply)

                # Save response
                st.session_state.messages.append({"role": "assistant", "content": reply})

            except Exception as e:
                st.error(f"Error: {e}")
