import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Roast & Masti AI", page_icon="🔥", layout="centered")

st.title("🔥 Roast & Reason AI")
st.write("Sawaal pooch, kaam ka jawaab bhi milega aur thodi beizzati bhi! 😉")

# New API Key
API_KEY = "AQ.Ab8RN6KQ0SKypBFYG4XkaqJHrRMKxjPS0HWqkkC09R6h4HsCPg"

# Setup Gemini
genai.configure(api_key=API_KEY)

system_instruction = """
Aap ek witty, thode savage aur sarcastic AI assistant ho.
Aapka kaam user ke sawaal ka bilkul sahi aur accurate jawaab dena hai, 
par jawaab dene se pehle ya baad me unka mazedaar roast/beizzati bhi karni hai.
Language Hinglish (Hindi + English) honi chahiye. Tone friendly, mazaak-masti wali aur entertaining honi chahiye.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction
)

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
        with st.spinner("Dimaag chala raha hoon... (aur beizzati soch raha hoon)"):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Kuch error aaya: {e}")
                
