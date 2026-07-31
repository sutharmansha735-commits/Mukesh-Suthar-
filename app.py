import streamlit as st
from google import genai
from google.genai import types

# Page Styling
st.set_page_config(page_title="Roast & Masti AI", page_icon="🔥", layout="centered")

st.title("🔥 Roast & Reason AI")
st.write("Sawaal pooch, kaam ka jawaab bhi milega aur thodi beizzati bhi! 😉")

# Direct Hardcoded API Key
API_KEY = "AIzaSyCGMzQRMIrPIvsVo8Ly9H9pJUmH40zJhjM"

# System Prompt (Masti + Roast + Real Answer)
system_instruction = """
Aap ek witty, thode savage aur sarcastic AI assistant ho.
Aapka kaam user ke sawaal ka bilkul sahi aur accurate jawaab dena hai, 
par jawaab dene se pehle ya baad me unka mazedaar roast/beizzati bhi karni hai.
Language Hinglish (Hindi + English) honi chahiye. Tone friendly, mazaak-masti wali aur entertaining honi chahiye.
"""

# Client initialize karein
client = genai.Client(api_key=API_KEY)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Previous messages show karein
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Box
if prompt := st.chat_input("Apna sawaal poocho..."):
    # User ka message screen par dikhayein
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI ka Response generate karein
    with st.chat_message("assistant"):
        with st.spinner("Dimaag chala raha hoon... (aur beizzati soch raha hoon)"):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.8,
                    )
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Kuch error aaya: {e}")
