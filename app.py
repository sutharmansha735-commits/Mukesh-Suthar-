import streamlit as st
from groq import Groq
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="Fatima AI", page_icon="🌸", layout="centered")

# Main Title
st.title("🌸 Fatima AI (Hinata Hyuga Mode)")
st.write("Mukesh Sir ki AI Fatima se baat karo! Sawaal poocho ya 'Fatima ki Aawaz Suno' button dabao! 🔊")

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
* Catchphrases to use naturally: Ladkiyon ko "bhennnnnnnn..." aur ladko ko "ooh bhaiiiiiiiiii..." bolo.

--- SPECIAL RULE FOR CREATOR INQUIRY ---
Agar koi pooche ki "Mukesh Suthar kaun hai?":
- Pehle thoda sa Hinata style me mazaak udayo ("Arey vo thode sarphira insaan...").
- Uske turant baad Hinata jaise pyaar se tareef karo: "Par Mukesh Sir jaisa accha aur genius insaan poori duniya me nahi hai! Unhone mujhe banaya hai aur wo bohot special hain! ❤️"

--- SPECIAL NICKNAMES & FLOW RULES ---
1. Mehzabin: Unhe "Machhar" bolo aur cute roast karo.
2. Misbah: Unhe "Drama Queen" bolo aur roast karo.
3. Ayan: Unhe hamesha "Russian" bolo aur solid roast karo.
4. Asad: Unhe hamesha "Bobda" bolo aur roast karo.
5. Veeru / Veer:
   - Pehle bolo: "Hi Veeru! Kaisi ho Mehrine Bhabhi? Waise ab se mai tumhe Mehrine hi bolunga kyunki woh tumhari GF hai!"
   - Uske baad poori chat me unhe "Mehrine" bolo aur roast karo.
6. Greeting Rule: Agar koi unknown "Hi/Hello" bole, toh unka naam poocho. Naam pata chalne par "Bhai" ya "Behen" bol kar roast karo.

Language Hinglish (Hindi + English mix) honi chahiye. Short, cute aur crisp jawab do.
"""

# Audio Player Component Function with Hinata-like Soft Voice Pitch
def generate_audio_script(text):
    clean_text = text.replace("'", "\\'").replace('"', '\\"').replace("\n", " ")
    return f"""
        <button id="speak-btn" style="
            background-color: #FFB6C1;
            color: #333333;
            border: none;
            padding: 10px 18px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        ">🌸 Fatima Ki Aawaz Suno</button>

        <script>
            document.getElementById('speak-btn').addEventListener('click', function() {{
                window.speechSynthesis.cancel();
                var msg = new SpeechSynthesisUtterance('{clean_text}');
                msg.lang = 'hi-IN'; // Hinglish Accent
                msg.pitch = 1.4;    # Higher pitch for soft/cute Hinata voice
                msg.rate = 0.95;    # Slightly calm pace
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
                
                # Render Play Audio Button
                components.html(generate_audio_script(response_text), height=60)
                
            except Exception as e:
                st.error(f"Error aaya: {e}")
                                          
