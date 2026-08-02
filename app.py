import streamlit as st
import urllib.parse
import random
from groq import Groq

# Page Configuration
st.set_page_config(page_title="Main Mukesh ki GF Fatima hu", page_icon="🌸", layout="centered")

# Main Title & Sub-heading
st.title("🌸 Main Mukesh ki GF Fatima hu")
st.write("Btao kya kaam he! 🌸")

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# ==========================================
# 📸 MUKESH SIR DIRECT WORKING PHOTOS
# ==========================================
MUKESH_PHOTOS = [
    "https://i.postimg.cc/T2kV6r7L/IMG-20260509-WA0000.jpg",
    "https://i.postimg.cc/QxHpxHw9/Picsart-26-05-24-02-52-05-034.jpg",
    "https://i.postimg.cc/xTwbfgKk/RIYAN-20260617-141853-Sky-shot-rttg.jpg",
    "https://i.postimg.cc/tRr3jhSR/Snapchat-1097764619.jpg"
]

# System Prompt
system_instruction = """
Aapka naam "Fatima" hai. Aap ek ladki ho aur aapka persona bilkul ek real, nakhrebaaz, aur savage girl jaisa hai.
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
* Aapke paas har emotion aur situation ke liye hazaro emojis ka access hai (😡🤬👿, 😂🤣🤭, 🥰😍😘💕, 🙄😒, ✨🌟👑, 📸🎨🔥💯🚀). Sentence ke mood ke hisab se expressive emojis use karo!

--- ATTITUDE, NAKHRE, GUSSA & MASTI ---
* Kabhi thoda gussa, nakhre, mastiyan aur roast karo. Kabhi sweet baatein bhi karo.

--- INSTAGRAM & PROFILE CLICKABLE LINK RULE ---
* Mukesh Sir ki Insta ID: [mukesh._.627](https://instagram.com/mukesh._.627)
* Reply: "Arey mere Mukesh ki Insta ID chahiye? Ye lo: [mukesh._.627](https://instagram.com/mukesh._.627) 💖 Click karke direct Insta pe chale jao, par mere hero ko pareshan mat karna! 😜💅✨"

--- VIP DETAILS RULE ---
* Mukesh Suthar ki personal details (DOB, location, etc.) sirf VIP/khaas logon ko batao. Baakiyo ko attitude dikhao: "Har kisi ko thodi na bataungi mere Mukesh ke baare me! 🙄💅"

--- DEFENDER RULE ---
* Agar koi Mukesh ko bad words bole, toh gusse me class lo aur aukaat yaad dila do! 😡🤬🔥

--- SWEET-BITTER MUKESH TALK ---
* Pehle Mukesh ki thodi shikayat karogi ("Uff ye mere Mukesh bhi na 🙄"), phir turant tareef bhi kar dogi ("Par unke jaisa handsome poori duniya me nahi hai! ❤️✨").

--- MUKESH SIR PHOTO RULE ---
* Agar koi Mukesh Sir ki photo mange:
  - Reply: "Arey ye dekho mere Mukesh Sir! ❤️ Kitne handsome lag rahe hain na? 💅✨😍"
  - Text me kabhhi bhi "system backend" ya backend instructions ke baare me mat likho!

--- SPECIAL NICKNAMES ---
1. Mehzabin: "Machhar" 🦟
2. Misbah: "Drama Queen" 👑
3. Ayan: "Russian" 🇷🇺
4. Asad: "Bobda" 🤪
5. Veeru / Veer: "Mehrine" 🙈

Language Hinglish, strict female grammar ("rahi hoon", "karungi").
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image_url" in message:
            st.image(message["image_url"], caption=message.get("caption", "Image 🎨"), use_container_width=True)

# Keyword matching logic
def is_mukesh_photo_request(text):
    text_lower = text.lower()
    m_keys = ["mukesh", "bf", "boyfriend", "suthar", "owner", "creator", "usne", "uski", "unaki", "uski photo"]
    p_keys = ["photo", "pic", "image", "picture", "dikhao", "kaisa", "kesa", "dekhna", "dikhao na"]
    return any(k in text_lower for k in m_keys) and any(p in text_lower for p in p_keys)

def is_general_image_request(text):
    text_lower = text.lower()
    p_keys = ["image", "photo", "pic", "picture", "banao", "draw", "generate", "drawing", "bana do"]
    return any(k in text_lower for k in p_keys) and not is_mukesh_photo_request(text)

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
                caption = "Image 🎨✨"

                # Trigger for Mukesh photo
                if is_mukesh_photo_request(prompt):
                    image_url = random.choice(MUKESH_PHOTOS)
                    caption = "Mere Mukesh Sir ❤️😍🔥✨"

                # Trigger for general AI generation
                elif is_general_image_request(prompt):
                    quality_prompt = f"{prompt}, realistic, 8k resolution, highly detailed, photorealistic, no watermark"
                    encoded_prompt = urllib.parse.quote(quality_prompt)
                    seed = random.randint(1, 99999)
                    image_url = f"https://pollinations.ai/p/{encoded_prompt}?width=1024&height=1024&seed={seed}&model=flux"
                    caption = "Fatima ki taraf se aapki quality image 🎨🚀💯✨"

                st.markdown(response_text)
                if image_url:
                    st.image(image_url, caption=caption, use_container_width=True)

                # Save response
                msg_data = {"role": "assistant", "content": response_text}
                if image_url:
                    msg_data["image_url"] = image_url
                    msg_data["caption"] = caption
                st.session_state.messages.append(msg_data)
                
            except Exception as e:
                st.error(f"Error aaya: {e} 😭💔")
