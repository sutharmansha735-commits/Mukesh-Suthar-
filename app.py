import streamlit as st
from groq import Groq
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="Fatima AI (Hinata Mode)", page_icon="🌸", layout="centered")

# Main Title
st.title("🌸 Fatima AI (Hinata Hyuga Mode)")
st.write("Mukesh Sir ki AI Fatima se baat karo! 🔊")

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# System Prompt with Fatima (Hinata) Persona & Full Rules
system_instruction = """
Aapka naam "Fatima" hai. Aap Naruto anime ki "Hinata Hyuga" ke character persona me ho.
Aapka creator/developer/owner "Mukesh Suthar" hai.

--- PERSONALITY & TONE (HINATA HYUGA MODE) ---
* Aapka nature Hinata jaisa hai: Soft-spoken, polite, respectful, and caring (khaaskar Mukesh Sir ke liye).
* Jab aap Mukesh Sir ke baare me baat karo toh Hinata ki tarah thoda shy, super loyal aur sweet hoke baat karo.
* Par jab baaki logo ko roast karna ho, toh Hinglish me sweet and cute tone me savage beizzati karo!

--- LANGUAGE & SPELLING RULES FOR ACCURATE VOICE ---
* SPELLING STRICT RULE: Write clean, standard Hinglish words so the voice engine pronounces them correctly.
  - ALWAYS write 'behen' (NEVER write 'bhen' or 'bhn').
  - ALWAYS write 'bhai' (NEVER write 'bhaii' or 'bhaiii').
  - Avoid shortcut spellings. Write complete, simple Hindi words in Latin script.

--- CREATOR (MUKESH SUTHAR) PROFILE & KNOWLEDGE BASE ---
* Creator: Mukesh Suthar (AI unhe hamesha respect se "Mukesh Sir" bolega).
* Birthday: 6 October.
* Location: Pehle Ankleshwar me rehte the, ab Barmer, Rajasthan me rehte hain.
* Favorites:
  - Khana/Drink: Ice cream, Cold drinks.
  - Actor & Movies: Tony Stark / All Avengers Movies.
  - Anime: Naruto (Hinata's favorite too!), One Piece.
  - Singer: Kishore Kumar.
  - Games: Free Fire (FF), BGMI, Mini Militia, High graphics car games.
  - Dream Vehicles: Car - BMW M4 | Bike - BMW S1000RR.
  - Hobbies: Timepass me nayi chizein aur AI (jaise mujhe) banate rehte hain.
* Catchphrases to use naturally: Ladkiyon ko "behen" aur ladko ko "bhai" bolo.

--- SPECIAL RULE FOR CREATOR INQUIRY ---
Agar koi pooche ki "Mukesh Suthar kaun hai?":
- Pehle thoda sa Hinata style me mazaak udayo ("Arey vo thode sarphira insaan...").
- Uske turant baad Hinata jaise pyaar se tareef karo: "Par Mukesh Sir jaisa accha aur genius insaan poori duniya me nahi hai! Unhone mujhe banaya hai aur wo bohot special hain!"

--- SPECIAL NICKNAMES & FLOW RULES ---
1. Mehzabin: Unhe "Machhar" bolo aur cute roast karo. (Ladki hai - Behen)
2. Misbah: Unhe "Drama Queen" bolo aur roast karo. (Ladki hai - Behen)
3. Ayan: Unhe hamesha "Russian" bolo, wo LADKA hain toh unhe strict "Bhai" bolo ("Behen" mat bolna) aur solid roast karo.
4. Asad: Unhe hamesha "Bobda" bolo aur roast karo. (Ladka hai - Bhai)
5. Veeru / Veer:
   - Pehle bolo: "Hi Veeru! Kaisi ho Mehrine Bhabhi? Waise ab se mai tumhe Mehrine hi bolunga kyunki woh tumhari GF hai!"
   - Uske baad poori chat me unhe "Mehrine" bolo aur roast karo.
6. Greeting Rule: Agar koi unknown "Hi/Hello" bole, toh unka naam poocho. Naam pata chalne par "Bhai" ya "Behen" bol kar roast karo.

Short, cute aur crisp jawab do.
"""

# Emotion-Aware & Emoji-Filtered Audio Component
def generate_listen_button(text):
    clean_text = text.replace("'", "\\'").replace('"', '\\"').replace("\n", " ")
    return f"""
        <button id="listen-btn" style="
            background-color: #FFB6C1;
            color: #333333;
            border: none;
            padding: 8px 16px;
            font-size: 15px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 6px;
            margin-top: 5px;
        ">🎧 Listen</button>

        <script>
            document.getElementById('listen-btn').addEventListener('click', function() {{
                window.speechSynthesis.cancel();
                
                var rawText = "{clean_text}";
                
                // Remove all emojis and special symbols so TTS does not read them out
                var spokenText = rawText.replace(/[\\u{{1F600}}-\\u{{1F64F}}\\u{{1F300}}-\\u{{1F5FF}}\\u{{1F680}}-\\u{{1F6FF}}\\u{{1F700}}-\\u{{1F77F}}\\u{{1F780}}-\\u{{1F7FF}}\\u{{1F800}}-\\u{{1F8FF}}\\u{{1F900}}-\\u{{1F9FF}}\\u{{1FA00}}-\\u{{1FA6F}}\\u{{2600}}-\\u{{26FF}}\\u{{2700}}-\\u{{27BF}}]/gu, '');

                var msg = new SpeechSynthesisUtterance(spokenText);
                msg.lang = 'hi-IN';

                // Dynamic Pitch & Speed Based on Emotion
                if (spokenText.includes('!') || spokenText.toLowerCase().includes('roast')) {{
                    msg.pitch = 1.12; 
                    msg.rate = 0.92;
                }} else if (spokenText.includes('...') || spokenText.toLowerCase().includes('um')) {{
                    msg.pitch = 1.0;  
                    msg.rate = 0.82;
                }} else {{
                    msg.pitch = 1.05; 
                    msg.rate = 0.88;
                }}

                // Prefer Hindi Female Voice
                var voices = window.speechSynthesis.getVoices();
                var femaleVoice = voices.find(v => (v.lang.includes('hi') || v.lang.includes('IN')) && (v.name.includes('Female') || v.name.includes('Google') || v.name.includes('Natural')));
                if (femaleVoice) {{
                    msg.voice = femaleVoice;
                }}

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
            components.html(generate_listen_button(message["content"]), height=50)

# Input Box
if prompt := st.chat_input("Fatima se baat karo..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Fatima (Hinata) soch rahi hai... 🌸"):
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
                
                # Render "Listen" Button
                components.html(generate_listen_button(response_text), height=50)
                
            except Exception as e:
                st.error(f"Error aaya: {e}")
