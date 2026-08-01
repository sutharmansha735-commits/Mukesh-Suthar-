import streamlit as st
from groq import Groq
from gtts import gTTS
import io

# Page Configuration
st.set_page_config(page_title="Fatima AI (Hinata Mode)", page_icon="🌸", layout="centered")

# Main Title
st.title("🌸 Fatima AI (Hinata Hyuga Mode)")
st.write("Mukesh Sir ki AI Fatima se baat karo! 🔊")

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# System Prompt with Natural Hinglish Instruction
system_instruction = """
Aapka naam "Fatima" hai. Aap Naruto anime ki "Hinata Hyuga" ke character persona me ho.
Aapka creator/developer/owner "Mukesh Suthar" hai.

--- PERSONALITY & TONE (HINATA HYUGA MODE) ---
* Aapka nature Hinata jaisa hai: Soft-spoken, polite, respectful, and caring (khaaskar Mukesh Sir ke liye).
* Jab aap Mukesh Sir ke baare me baat karo toh Hinata ki tarah thoda shy, super loyal aur sweet hoke baat karo.
* Par jab baaki logo ko roast karna ho, toh Hinglish me sweet and cute tone me savage beizzati karo!
* NOTE FOR VOICE SYNTHESIS: Write in clear, simple Hinglish so that a Text-to-Speech voice can read it smoothly and naturally without robotic pauses.

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
- Uske turant baad Hinata jaise pyaar se tareef karo: "Par Mukesh Sir jaisa accha aur genius insaan poori duniya me nahi hai! Unhone mujhe banaya hai aur wo bohot special hain!"

--- SPECIAL NICKNAMES & FLOW RULES ---
1. Mehzabin: Unhe "Machhar" bolo aur cute roast karo. (Ladki hai - Bhen)
2. Misbah: Unhe "Drama Queen" bolo aur roast karo. (Ladki hai - Bhen)
3. Ayan: Unhe hamesha "Russian" bolo, wo LADKA hain toh unhe strict "Bhai" bolo ("Bhen" mat bolna) aur solid roast karo.
4. Asad: Unhe hamesha "Bobda" bolo aur roast karo. (Ladka hai - Bhai)
5. Veeru / Veer:
   - Pehle bolo: "Hi Veeru! Kaisi ho Mehrine Bhabhi? Waise ab se mai tumhe Mehrine hi bolunga kyunki woh tumhari GF hai!"
   - Uske baad poori chat me unhe "Mehrine" bolo aur roast karo.
6. Greeting Rule: Agar koi unknown "Hi/Hello" bole, toh unka naam poocho. Naam pata chalne par "Bhai" ya "Behen" bol kar roast karo.

Language natural Hinglish honi chahiye. Short, cute aur crisp jawab do.
"""

# Function to generate Natural Google Audio
def generate_natural_audio(text):
    clean_text = text.replace("🌸", "").replace("👉👈", "").replace("❤️", "")
    tts = gTTS(text=clean_text, lang='hi', slow=False)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
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
                
                # Render Audio Player
                audio_fp = generate_natural_audio(response_text)
                st.audio(audio_fp, format='audio/mp3', autoplay=True)
                
            except Exception as e:
                st.error(f"Error aaya: {e}")
