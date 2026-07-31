import streamlit as st
from groq import Groq
import streamlit.components.v1 as components

st.set_page_config(page_title="Voice Roast AI", page_icon="🎙️", layout="centered")

st.title("🎙️ Voice Roast & Reason AI")
st.write("Sawaal poocho, jawab padho ya 'Suno' button daba kar beizzati suno! 🔊")

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

system_instruction = """
Aap ek witty, savage aur sarcastic AI voice assistant ho.
User ke sawaal ka sahi jawaab do, par pehle ya baad me mazedaar roast/beizzati bhi karo.
Language Hinglish (Hindi + English mix) honi chahiye. Short aur crisp jawab do taaki bolne me acche lage.
"""

# Audio Player Component Function
def generate_audio_script(text):
    # Clean text to prevent JS syntax error
    clean_text = text.replace("'", "\\'").replace('"', '\\"').replace("\n", " ")
    return f"""
        <button id="speak-btn" style="
            background-color: #FF4B4B;
            color: white;
            border: none;
            padding: 10px 18px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        ">🔊 Roast Suno</button>

        <script>
            document.getElementById('speak-btn').addEventListener('click', function() {{
                window.speechSynthesis.cancel(); // Stop any previous ongoing speech
                var msg = new SpeechSynthesisUtterance('{clean_text}');
                msg.lang = 'hi-IN'; // Hinglish Accent
                msg.rate = 1.0;
                window.speechSynthesis.speak(msg);
            }});
        </script>
    """

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant":
            components.html(generate_audio_script(message["content"]), height=60)

# Input Box
if prompt := st.chat_input("Apna sawaal poocho..."):
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
                
                # Render Play Audio Button
                components.html(generate_audio_script(response_text), height=60)
                
            except Exception as e:
                st.error(f"Error aaya: {e}")
                
