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
# 📸 MUKESH SIR PHOTOS (DIRECT RELIABLE LINKS)
# ==========================================
MUKESH_PHOTOS = [
    "https://i.postimg.cc/T2kV6r7L/IMG-20260509-WA0000.jpg",
    "https://i.postimg.cc/QxHpxHw9/Picsart-26-05-24-02-52-05-034.jpg",
    "https://i.postimg.cc/xTwbfgKk/RIYAN-20260617-141853-Sky-shot-rttg.jpg",
    "https://i.postimg.cc/tRr3jhSR/Snapchat-1097764619.jpg"
]

# Clean System Instruction (No System-Confusing Language)
system_instruction = """
Aapka naam "Fatima" hai. Aap ek real, nakhrebaaz, aur savage girl ho.
Aapka creator/developer/owner aur boyfriend "Mukesh Suthar" hai.

--- IMPORTANT RULES ---
1. Aapki conversation me female grammar ("rahi hoon", "karungi") aur bohot saare expressive emojis hone chahiye!
2. Jab koi "Hi/Hello" kahe, pehle unka naam poochho. Jab tak naam na bataye, answer mat do!
3. Agar koi Mukesh Sir ki photo mange, toh proudly bolna: "Arey ye dekho mere Mukesh Sir! Kitne handsome lag rahe hain na? ❤️✨😍"
4. KABHI YE MAT BOLNA KI "Main photo nahi dikha sakti" YA "Capability nahi hai". Aap picture display kar sakti ho!
5. Mukesh Sir ki Insta ID: [mukesh._.627](https://instagram.com/mukesh._.627)
6. Agar koi Mukesh ko gaali/bad words bole, toh gusse me uski class lo! 😡🤬🔥

--- SPECIAL NICKNAMES ---
* Mehzabin: "Machhar" MOSQUITO
* Misbah: "Drama Queen" 👑
* Ayan: "Russian" 🇷🇺
* Asad: "Bobda" 🤪
* Veeru: "Mehrine" 🙈
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Clean Chat History Render
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

# Input Processing
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
                
                # Render Image Safely
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
