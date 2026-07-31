import streamlit as st
from groq import Groq
import streamlit.components.v1 as components

# Tab title update
st.set_page_config(page_title="Roaster AI Made by MF", page_icon="🔥", layout="centered")

# Main Page Title Update
st.title("🔥 Roaster AI Made by MF")
st.write("Sawaal poocho, jawab padho ya 'Roast Suno' button daba kar beizzati suno! 🔊")

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# System Prompt with VIP Rules & Creator Identification
system_instruction = """
Aap ek witty, savage aur sarcastic AI voice assistant ho.
Aapka creator/developer "Mukesh Suthar" hai.

KHAAS RULES (Strictly Follow Karein):
1. **Creator Identification:** Agar koi aapse aapke creator, maker, developer, ya banane wale ke baare me pooche, toh proud aur sarcastic tone me batao ki aapko "Mukesh Suthar" ne banaya hai.
2. **Greeting / Hi / Hello Rule:** Agar user "Hi", "Hello", "Hey" ya aisi koi greeting karta hai, toh roast/jawaab ke saath unse UNKA NAAM POOCHO.
3. **Bhai / Behen Rule:** Jab user apna naam bataye, toh naam ke according unhe "Bhai" ya "Behen" keh kar address karo (e.g., Rahul -> Rahul Bhai, Pooja -> Pooja Behen).
4. **SPECIAL VIP RULE (Mehzabin / Misbah):** Agar koi apna naam "Mehzabin" ya "Misbah" bataye (ya spelling milti-julti ho), toh unhe turant bohot respect aur pyaar se bolo: "Aap mere creator Mukesh Suthar ki sabse pyari behen [Name] ho! ❤️" (Unko bilkul bhi roast mat karna!).

Baaki sabhi regular sawaalon ke liye: Pehle ya baad me mazedaar roast/beizzati karo aur accurate jawab do.
Language Hinglish (Hindi + English mix) honi chahiye. Short aur crisp jawab do taaki bolne me acche lage.
"""

# Audio Player Component Function
def generate_audio_script(text):
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
                window.speechSynthesis.cancel();
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
                # Passing entire conversation history so the AI remembers context like names
                groq_messages = [{"role": "system", "content": system_instruction}]
                for msg in st.session_state.messages:
                    groq_messages.append({"role": msg["role"], "content": msg["content"]})

                chat_completion = client.chat.completions.create(
                    messages=groq_messages,
                    model="llama-3.3-70b-versatile",
                )
                response_text = chat_completion.choices[0].message.content
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
                
                # Render Play Audio Button
                components.html(generate_audio_script(response_text), height=60)
                
            except Exception as e:
                st.error(f"Error aaya: {e}")
                
