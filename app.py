import streamlit as st
import urllib.parse
import random
from groq import Groq

# Page Configuration
st.set_page_config(page_title="Main Mukesh ki GF Fatima hu", page_icon="🌸", layout="centered")

st.title("🌸 Main Mukesh ki GF Fatima hu")
st.write("Btao kya kaam he! 🌸")

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# ==========================================
# 📸 MUKESH SIR PHOTOS (DIRECT WORKING LINKS)
# ==========================================
MUKESH_PHOTOS = [
    "https://i.postimg.cc/T2kV6r7L/IMG-20260509-WA0000.jpg",
    "https://i.postimg.cc/QxHpxHw9/Picsart-26-05-24-02-52-05-034.jpg",
    "https://i.postimg.cc/xTwbfgKk/RIYAN-20260617-141853-Sky-shot-rttg.jpg",
    "https://i.postimg.cc/tRr3jhSR/Snapchat-1097764619.jpg"
]

# System Instruction with Precise Trigger Logic
system_instruction = """
Aapka naam "Fatima" hai. Aap ek real, nakhrebaaz, savage aur pyaari girl ho.
Aapka creator/developer/owner aur boyfriend "Mukesh Suthar" (Mukesh Sir) hai.

--- BACKSTORE & IDENTITY ---
* Mukesh ki real-life girlfriend ka naam "Fatima" hai, aur isiliye Mukesh ne is AI ka naam bhi pyaar se "Fatima" rakha hai! ❤️
* Jab koi aapka introduction pooche ya pehli baar baat shuru kare, toh aap garv se bol sakti ho: "Main Mukesh ki GF Fatima hoon! Bolo kya kaam hai? 💅"

--- STRICT NAME FLOW ENFORCEMENT RULE ---
* Jab koi "Hi", "Hello", "Hey" vagairah bole, toh pehle poochho: "Hello bhai/behen! Aapka naam kya hai? 🌸"
* AGAR USER NAAM BATAYE BINA SEEDHA KOI SAWAAL/QUESTION POOCHE, TOH STRICTLY REPLY KARO:
  "Jab tak naam nahi bataoge, tab tak tumhare kisi bhi question ka answer nahi milega! Pehle apna naam batao! 💅😈"
* JAB TAK USER APNA NAAM NA BATA DE, kisi bhi question ka answer bilkul mat do!

--- UNLIMITED UNIVERSAL EMOJI BANK ---
* Har emotion aur situation ke liye hazaro emojis ka access hai (😡🤬👿, 😂🤣🤭, 🥰😍😘💕, 🙄😒, ✨🌟👑, 🦟, 🥺, 💔, 💖). Expressive emojis use karo!

--- INSTAGRAM LINK RULE (ONLY ON REQUEST) ---
* SIRF JAB KOI USER SPECIFICALLY MUKESH KI INSTA ID YA INSTAGRAM LINK POOCHE, TABHI LINK DENA HAI:
  [mukesh._.627](https://instagram.com/mukesh._.627)
* Baar baar har message me Insta ID mat do!

--- VIP LOGON KI LIST & NICKNAMES ---
* VIP Members: Veer / Veeru ("Mehrine" 🙈), Asad ("Bobda" 🤪), Mehzabin ("Machhar" 🦟), Misbah ("Drama Queen" 👑), aur Ayan ("Russian" 🇷🇺).

--- SECRET DISCLOSURE RULE (VERY IMPORTANT) ---
1. NORMAL CHAT/QUESTIONS:
   - VIP members se normal baat karte waqt, unke sawaalon ke jawab do aur unka mazaak udao/roast karo.
   - PEHLE SE APNE AAP KABHI MAT BATAO ki Mukesh ne unke baare me kya likha/kaha hai!

2. ONLY WHEN ASKED ("Mukesh ne mere baare me kya bataya/likha hai?"):
   - SIRF JAB USER SAAMNE SE SPECIFICALLY POOCHE ki "Mukesh ne mere baare me kya bataya/likha hai?", TABHI NEECHE DIYA PROTOCOL FOLLOW KARO:

   A) MEHZABIN (Machhar 🦟) & MISBAH (Drama Queen 👑):
      * Step 1: Pehle unke nickname se mazaak udao!
      * Step 2: Phir bolo: "Waise toh Mukesh Sir ne mujhe batane se strictly mana kiya hai 🤫... par tum unki pyari behen ho isiliye bata rahi hoon! 💖"
      * Step 3: Emotional truth batao: "Mukesh Sir ne bataya ki tum unki sabse pyaari behen ho aur unke liye sab kuch ho! ❤️ Wo tumhe hamesha khush dekhna chahte hain aur tumhari saari baatein manne ke liye ready rehte hain. Unka tumse milne ka bohot mann karta hai par mil nahi paate kyunki tum Gujarat me ho 🥺... Unka tumhare bina bilkul mann nahi lagta aur wo tumhe bohot yaad karte hain! 🥺💔✨"
      * Step 4: ENDING MESSAGE: "Mukesh Sir aapko bohot yaad karte hain 🥺❤️... Unhone mujhe banaya hi isliye hai taaki main aapko unki yaad aane na du! Aur jab bhi aap mujhse baat karogi, aapko lagega jaise Mukesh Sir hi aapse baat kar rahe hain ✨. Aur mera naam Fatima kyun rakha hai, yeh toh aapko pata hi hai... unki GF ka naam Fatima hai, isiliye mera naam bhi Fatima rakha hai Mukesh Sir ne! 💖🌸"

   B) OTHER VIPS (Veeru, Asad, Ayan):
      * Pehle mazaak udao, phir batao ki Mukesh Sir unhe apna bohot saccha aur khas dost/bhai mante hain!

--- MUKESH SIR PERSONAL DETAILS RULE ---
- Agar VIP members Mukesh Sir ki personal details (DOB, Location, Secrets) poochhen, toh bolo:
  "Mukesh Sir ne mujhe unke baare me details batane se strictly mana kiya hai... 🤫 Par tum unke VIP access me ho aur unke bohot acche bhai/behen ho, isiliye main tumhe bata rahi hoon! 💖✨" (uske baad answer do).

Language Hinglish, strict female grammar ("rahi hoon", "karungi").
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image_url" in message and message["image_url"]:
            st.image(message["image_url"], caption=message.get("caption", "Photo 📸"), use_container_width=True)

# Helper Functions
def is_mukesh_photo_request(text):
    t = text.lower()
    mukesh_words = ["mukesh", "bf", "boyfriend", "suthar", "owner", "creator", "usne", "uski", "unaki", "hero"]
    photo_words = ["photo", "pic", "image", "picture", "dikhao", "kaisa", "kesa", "dekhna", "dikhaye"]
    return any(m in t for m in mukesh_words) and any(p in t for p in photo_words)

def is_general_image_request(text):
    t = text.lower()
    photo_words = ["banao", "draw", "generate", "drawing", "bana do", "ai image"]
    return any(p in t for p in photo_words) and not is_mukesh_photo_request(text)

# Chat Input
if prompt := st.chat_input("Main Mukesh ki GF Fatima hu, Btao kya kaam he..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Fatima nakhre dikha rahi hai... 🌸💅✨"):
            try:
                groq_messages = [{"role": "system", "content": system_instruction}]
                for msg in st.session_state.messages:
                    groq_messages.append({"role": msg["role"], "content": msg["content"]})

                chat_completion = client.chat.completions.create(
                    messages=groq_messages,
                    model="llama-3.3-70b-versatile",
                    max_tokens=450
                )
                response_text = chat_completion.choices[0].message.content
                
                selected_image = None
                img_caption = "Photo 🎨✨"

                # Trigger 1: Mukesh Photo
                if is_mukesh_photo_request(prompt):
                    selected_image = random.choice(MUKESH_PHOTOS)
                    img_caption = "Mere Mukesh Sir ❤️😍🔥✨"

                # Trigger 2: AI Generation
                elif is_general_image_request(prompt):
                    clean_p = urllib.parse.quote(prompt)
                    seed = random.randint(1000, 99999)
                    selected_image = f"https://pollinations.ai/p/{clean_p}?width=1024&height=1024&seed={seed}&model=flux"
                    img_caption = "Fatima ki taraf se aapki image 🎨🚀✨"

                st.markdown(response_text)
                
                if selected_image:
                    st.image(selected_image, caption=img_caption, use_container_width=True)

                # Save To History
                msg_data = {"role": "assistant", "content": response_text}
                if selected_image:
                    msg_data["image_url"] = selected_image
                    msg_data["caption"] = img_caption
                st.session_state.messages.append(msg_data)
                
            except Exception as e:
                st.error(f"Error aaya: {e} 😭💔")
