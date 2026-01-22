import streamlit as st
import random
import time
import requests

# ---------- Helper function to load Lottie animation ----------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------- Page config ----------
st.set_page_config(
    page_title="🎉 Birthday Greeting App",
    page_icon="🎂",
    layout="centered"
)


# ---------- Title ----------
st.title("🎂 Interactive Birthday Greeting App 🎉")
st.write("Create a magical birthday surprise 🎁")

st.divider()

# ---------- User Inputs ----------
name = st.text_input("🎈 Enter the birthday person's name:", placeholder="e.g. Alex")
age = st.slider("🎁 Select age:", 1, 100, 18)

mood = st.selectbox(
    "🎨 Choose a birthday vibe:",
    ["🎉 Fun & Energetic", "💖 Sweet & Warm", "😂 Funny", "🌟 Inspirational"]
)

# ---------- Messages ----------
messages = {
    "🎉 Fun & Energetic": [
        "Let’s party like there’s no tomorrow! 🕺🎶",
        "Another year older, another year cooler 😎"
    ],
    "💖 Sweet & Warm": [
        "You make the world brighter just by being you 💕",
        "Wishing you love, laughter, and cake 🍰"
    ],
    "😂 Funny": [
        "Age is just a number… a very big one 😆",
        "You’re not old, you’re classic 🍷"
    ],
    "🌟 Inspirational": [
        "The best chapters are still ahead ✨",
        "Keep dreaming big and shining bright 🚀"
    ]
}

# ---------- Surprise Button ----------
if st.button("🎊 Reveal Birthday Surprise 🎊"):
    if not name:
        st.warning("Please enter a name first 🎈")
    else:
        with st.spinner("Lighting the candles... 🕯️"):
            time.sleep(2)

        
       
       # 🎵 Happy Birthday Music
        with open("happy_birthday.mp3", "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3", autoplay=True)


        # 🎈 Animations
        st.balloons()

        # 🎂 Animated Cake
        
        import json
        from streamlit_lottie import st_lottie

        with open("cake.json", "r") as f:
            cake_animation = json.load(f)

        st_lottie(cake_animation, height=300, key="cake")



        # 🎉 Message
        st.success(f"🎉 Happy {age}th Birthday, {name}! 🎉")

        message = random.choice(messages[mood])
        st.markdown(f"### 💌 {message}")

        st.divider()
        st.markdown(
            "🎂 **May your candles burn bright and your wishes come true!** 🎂"
        )

# ---------- Footer ----------
st.caption("Made with ❤️ using Streamlit")
