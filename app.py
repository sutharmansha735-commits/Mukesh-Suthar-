import streamlit as st
from groq import Groq

# Page Config
st.set_page_config(page_title="Roast & Masti AI", page_icon="🔥", layout="centered")

st.title("🔥 Roast & Reason AI")
st.write("Sawaal pooch, kaam ka jawaab bhi milega aur thodi beizzati bhi! 😉")

# Groq API Key
GROQ_API_KEY = "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"

# Initialize Client
client = Groq(api_key=GROQ_API_KEY)

# System Prompt
system_instruction = """
Aap ek witty, thode savage aur sarcastic AI assistant ho.
Aapka kaam user ke sawaal ka bilkul sahi aur accurate jawaab dena hai, 
par jawaab dene se pehle ya baad me unka mazedaar roast/beizzati bhi karni hai.
Language Hinglish (Hindi + English) honi chahiye. Tone friendly, mazaak-masti wali aur entertaining honi chahiye.
"""

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Apna sawaal poocho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Dimaag chala raha hoon... (aur roast soch raha hoon)"):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": prompt}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                response_text = chat_completion.choices[0].message.content
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"Kuch error aaya: {e}")
