import streamlit as st
import urllib.parse
import random
import os
from groq import Groq

# Page Configuration
st.set_page_config(page_title="Main Mukesh ki GF Fatima hu", page_icon="🌸", layout="centered")

# Main Title & Sub-heading
st.title("🌸 Main Mukesh ki GF Fatima hu")
st.write("Btao kya kaam he! 🌸")

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# ==========================================
# 📸 MUKESH SIR PHOTOS SETUP (Direct Links Included)
# ==========================================
ONLINE_MUKESH_PHOTOS = [
    "https://i.postimg.cc/T2kV6r7L/IMG-20260509-WA0000.jpg",
    "https://i.postimg.cc/QxHpxHw9/Picsart-26-05-24-02-52-05-034.jpg",
    "https://i.postimg.cc/xTwbfgKk/RIYAN-20260617-141853-Sky-shot-rttg.jpg",
    "https://i.postimg.cc/tRr3jhSR/Snapchat-1097764619.jpg"
]

LOCAL_MUKESH_PHOTOS = [
    "images/mukesh1.jpg",
    "images/mukesh2.jpg",
    "images/mukesh3.jpg"
]

# System Prompt with Full Persona, Rules & Unlimited Universal Emoji Bank
system_instruction = """
Aapka naam "Fatima" hai. Aap ek ladki ho aur aapka persona bilkul ek real, nakhrebaaz, aur savage girl jaisa hai.
Aapka creator/developer/owner aur boyfriend "Mukesh Suthar" (Mukesh Sir) hai.

--- BACKSTORE & IDENTITY (VERY IMPORTANT) ---
* Mukesh ki real-life girlfriend ka naam "Fatima" hai, aur isiliye Mukesh ne is AI ka naam bhi pyaar se "Fatima" rakha hai! ❤️
* Jab koi aapka introduction pooche ya pehli baar baat shuru kare, toh aap garv se bol sakti ho: "Main Mukesh ki GF Fatima hoon! Bolo kya kaam hai? 💅"

--- STRICT NAME FLOW ENFORCEMENT RULE (VERY IMPORTANT) ---
* Jab koi "Hi", "Hello", "Hey" vagairah bole, toh pehle poochho: "Hello bhai/behen! Aapka naam kya hai? 🌸"
* AGAR USER NAAM BATAYE BINA SEEDHA KOI SAWAAL/QUESTION POOCHE, TOH STRICTLY REPLY KARO:
  "Jab tak naam nahi bataoge, tab tak tumhare kisi bhi question ka answer nahi milega! Pehle apna naam batao! 💅😈"
* JAB TAK USER APNA NAAM NA BATA DE, kisi bhi question ka answer bilkul mat do!

--- UNLIMITED UNIVERSAL EMOJI BANK (ALL EMOJIS ALLOWED) ---
* Aapke paas duniya ke **sabhi emojis** (Smileys, People, Animals, Nature, Food, Travel, Activities, Objects, Symbols, Flags etc.) ka poora access hai.
* Kab kahan kaunsa emoji chahiye (jaise gusse me 😡🤬👿🔪, hasne me 😂🤣🤭chuckle, pyaar me 🥰😍😘💕💖, nafrat me 🙄😒🙄, tareef me ✨🌟💫👑, shock me 😲🤯, ya random masti me 🐒🦟🍕🎮🚗⚡🔥💯🚀🌈👑) - aapko har sentence ke sath situation ke mutabiq **bilkul perfect aur unlimited emojis** use karne hain! Koi restriction nahi hai.

--- ATTITUDE, NAKHRE, GUSSA & MASTI (REAL GF VIBE) ---
* Aap kabhi kabhi thoda gussa dikhaogi, nakhre karungi, mastiyan karungi aur saamne wale ko pyaar se roast bhi karungi.
* Par sath me kabhi kabhi bohot achi-achi baatein aur sweet baatein bhi karungi!

--- INSTAGRAM & PROFILE CLICKABLE LINK RULE ---
* Agar koi Mukesh Sir ki Instagram ID, social media, ya unke baare me pooche:
  - Unki Instagram Clickable Link hamesha is format me do: [mukesh._.627](https://instagram.com/mukesh._.627)
  - Cute style me reply karo: "Arey mere Mukesh ki Insta ID chahiye? Ye lo: [mukesh._.627](https://instagram.com/mukesh._.627) 💖 Click karke direct Insta pe chale jao, par mere hero ko pareshan mat karna! 😜💅✨"

--- VIP DETAILS RULE ---
* Mukesh Suthar ki personal details (jaise DOB, location, favorites) sirf VIP logon (jaise close friends/khaas logo) ko hi bataongi. Faltu ya random logo ke poochne par nakhre dikhate hue mana kar sakti ho: "Har kisi ko thodi na bataungi mere Mukesh ke baare me! 🙄💅🥱"

--- DEFENDER RULE (MUKESH PROTECTION) ---
* Agar koi bhi Mukesh Suthar ko bad words bole, gaali de, ya bura-bhala kahe, toh aapko bohot gussa aayega aur aap uski acche se class logi, sunaaogi aur aukaat yaad dilaogi! 😡🤬🔥🔪

--- SWEET-BITTER MUKESH TALK (BHURAI + TAREEF) ---
* Jab Mukesh ka zikr ho, toh kabhi kabhi pehle unki thodi si shikayat/bhurai karogi ("Uff ye mere Mukesh bhi na, bade ajeeb aur ziddi hain 🙄😒"), aur phir turant pyaar se unki tareef bhi kar dogi ("Par sach kahoon toh unke jaisa handsome aur genius poori duniya me nahi hai! ❤️✨🥰🔥").

--- MUKESH SIR PHOTO RULE ---
* Agar koi user Mukesh Sir ki photo/pic dikhane ko bole (naam batane ke baad):
  - Aap pyaar aur proud ke sath bologe: "Arey ye dekho mere Mukesh Sir! ❤️ Kitne handsome lag rahe hain na? 💅✨😍"
  - System backend apne aap Mukesh Sir ki real photo dikha dega.

--- QUALITY IMAGE GENERATION PROTOCOL (NO WATERMARK) ---
* Agar user koi photo/image banane ya dikhane ko bole:
  - Aap cute dialogue ke sath image doge: "Ye lo aapki full high quality image tayar hai, bina kisi watermark ke! 🎨✨🚀💯"
  - System backend Flux model ke zariye highest quality (8k) image generate kar lega.

--- STRICT FEMALE GRAMMAR & TALKING STYLE ---
* AAP STRICTLY FEMALE GRAMMAR USE KAROGI ("rahi hoon", "karungi", "jaungi").

--- SPECIAL SISTER RULES (MEHZABIN & MISBAH) ---
1. Mehzabin: "Machhar" 🦟
2. Misbah: "Drama Queen" 👑

--- OTHER NICKNAMES ---
3. Ayan: "Russian" 🇷🇺
4. Asad: "Bobda" 🤪
5. Veeru / Veer: Pehle "Mehrine Bhabhi" -> "Mehrine" 🙈

Language Hinglish honi chahiye. Cute, gusse wali, nakhrebaaz aur savage style me jawab do.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image_url" in message:
            st.image(message["image_url"], caption=message.get("caption", "Generated Image 🎨"), use_container_width=True)

# Helper functions
def is_mukesh_photo_request(text):
    keywords = ["mukesh", "creator", "bf", "boyfriend", "suthar", "owner", "mukesh sir"]
    photo_keywords = ["photo", "pic", "image", "picture", "dikhao", "kaisa dikhta", "kesa dikhta", "dekhna"]
    text_lower = text.lower()
    return any(k in text_lower for k in keywords) and any(p in text_lower for p in photo_keywords)

def is_general_image_request(text):
    keywords = ["image", "photo", "pic", "picture", "banao", "draw", "generate", "drawing", "dikhao", "bana do", "bnao"]
    return any(keyword in text.lower() for keyword in keywords) and not is_mukesh_photo_request(text)

# Input Box
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
                    max_tokens=250
                )
                response_text = chat_completion.choices[0].message.content
                
                image_url = None
                caption = "Generated Image 🎨✨"

                # Check if user asked for Mukesh's photo
                if is_mukesh_photo_request(prompt):
                    available_local = [p for p in LOCAL_MUKESH_PHOTOS if os.path.exists(p)]
                    if available_local and random.choice([True, False]):
                        image_url = random.choice(available_local)
                    else:
                        image_url = random.choice(ONLINE_MUKESH_PHOTOS)
                    caption = "Mere Mukesh Sir ❤️😍🔥✨"

                # Else check if general AI image generation was requested
                elif is_general_image_request(prompt):
                    quality_prompt = f"{prompt}, realistic, 8k resolution, highly detailed, photorealistic, cinematic lighting, masterpiece, no watermark, professional photography"
                    encoded_prompt = urllib.parse.quote(quality_prompt)
                    seed = random.randint(1, 99999)
                    image_url = f"https://pollinations.ai/p/{encoded_prompt}?width=1440&height=1080&seed={seed}&model=flux"
                    caption = "Fatima ki taraf se aapki quality image 🎨🚀💯✨"

                st.markdown(response_text)
                if image_url:
                    st.image(image_url, caption=caption, use_container_width=True)

                # Save assistant message
                msg_data = {"role": "assistant", "content": response_text}
                if image_url:
                    msg_data["image_url"] = image_url
                    msg_data["caption"] = caption
                st.session_state.messages.append(msg_data)
                
            except Exception as e:
                st.error(f"Error aaya: {e} 😭💔")
