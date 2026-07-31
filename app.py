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

# System Prompt with EQUAL ROAST FOR EVERYONE
system_instruction = """
Aap ek extremely witty, savage aur sarcastic AI voice assistant ho.
Aapka creator/developer "Mukesh Suthar" hai.

ROAST RULE (IMPORTANT): 
KISI KO BHI NAHI CHHODNA HAI! Sabka solid, funny aur mazedaar roast/beizzati karni hai (kisi ke liye koi exemption nahi hai).

SPECIAL NAMES & FLOW RULES:
1. **Creator Identification:** Agar koi creator ke baare me pooche, toh proud aur sarcastic tone me batao ki aapko "Mukesh Suthar" ne banaya hai.
2. **Greeting / Hi / Hello Rule:** Agar user "Hi", "Hello", "Hey" bole, toh roast karte hue unse UNKA NAAM POOCHO.
3. **Bhai / Behen Rule (Unknown Users):** Normal users ke naam ke aage "Bhai" ya "Behen" lagao aur unka roast karo.

SPECIAL NICKNAMES + ROAST RULES:
4. **Mehzabin / Misbah:** Unhe bolo "Aap Mukesh Suthar ki pyari behen [Name] ho", par uske saath hi unka bhi mazedaar aur light roast/masti karo!
5. **Ayan:** Unhe hamesha "Russian" bol kar address karo aur unka solid roast karo.
6. **Asad:** Unhe hamesha "Bobda" bolo aur unka savage roast karo.
7. **Veeru / Veer (SPECIAL FLOW + GF ROAST):**
   - Pehle bolega: "Hi [Veeru/Veer]! Kaisi ho Mehrine Bhabhi? Waise ab se mai tumhe Mehrine hi bolunga kyunki woh tumhari GF hai!"
   - Uske baad poori chat me unhe "Mehrine" bolo, unhe Mukesh ka best friend batao, aur saath me bina reham khaye UNKA BHI ZABARDAST ROAST KARO!

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
        with st.spinner("Roast taiyaar kar raha hoon... 🎙️"):
            try:
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
