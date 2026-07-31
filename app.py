import streamlit as st
from groq import Groq
import streamlit.components.v1 as components

st.set_page_config(page_title="Voice Roast AI", page_icon="🎙️", layout="centered")

st.title("🎙️ Voice Roast & Reason AI")
st.write("Bol kar sawaal poocho, AI bol kar hi jawab + roast dega! 🔊")

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

system_instruction = """
Aap ek witty, savage aur sarcastic AI voice assistant ho.
User ke sawaal ka sahi jawaab do, par pehle ya baad me mazedaar roast/beizzati bhi karo.
Hinglish (Hindi + English mix) me bolo. Short aur crisp jawab do taaki bolne me acche lage.
"""

# Text-To-Speech (Bolne ke liye JavaScript function)
def speak_text(text):
    # Special characters clean-up for safe JavaScript Execution
    clean_text = text.replace("'", "\\'").replace("\n", " ")
    js_code = f"""
        <script>
            var msg = new SpeechSynthesisUtterance('{clean_text}');
            msg.lang = 'hi-IN'; // Hindi-English tone
            msg.rate = 1.0;     # Speed
            window.speechSynthesis.speak(msg);
        </script>
    """
    components.html(js_code, height=0)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Likh kar ya mic se poocho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Soch raha hoon... 🎙️"):
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
                
                # Audio bol kar sunayein
                speak_text(response_text)
                
            except Exception as e:
                st.error(f"Error aaya: {e}")
                
