import streamlit as st
import random
import time
import requests
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from io import BytesIO
import os

def generate_birthday_pdf(name, age, message):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    half_width = width / 2

    # 🎨 Background
    c.setFillColor(HexColor("#FFF8E1"))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # ───────────── FRONT COVER (RIGHT PANEL) ─────────────
    c.setFillColor(white)
    c.roundRect(
        half_width + 1*cm,
        1.5*cm,
        half_width - 2*cm,
        height - 3*cm,
        20,
        fill=1,
        stroke=0
    )

    c.setFont("Helvetica-Bold", 30)
    c.setFillColor(HexColor("#D84315"))
    c.drawCentredString(half_width + half_width/2, height - 4.5*cm, "Happy Birthday!")

    # 🎂 Image
    image_path = "birthday_card.PNG"
    if os.path.exists(image_path):
        c.drawImage(
            image_path,
            half_width + 2.5*cm,
            height - 14*cm,
            width=half_width - 5*cm,
            height=7*cm,
            preserveAspectRatio=True,
            mask="auto"
        )

    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#6A1B9A"))
    c.drawCentredString(
        half_width + half_width/2,
        4*cm,
        f"For {name}"
    )

    # ───────────── INSIDE LEFT PANEL ─────────────
    c.setFillColor(white)
    c.roundRect(
        1*cm,
        1.5*cm,
        half_width - 2*cm,
        height - 3*cm,
        20,
        fill=1,
        stroke=0
    )

    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(HexColor("#00897B"))
    c.drawCentredString(half_width / 2, height - 5*cm, f"{age} Years Young")

    c.setFont("Helvetica-Oblique", 16)
    c.setFillColor(HexColor("#4E342E"))
    c.drawCentredString(
        half_width / 2,
        height - 7*cm,
        "A day just for you"
    )

    # ───────────── INSIDE RIGHT PANEL (MAIN MESSAGE) ─────────────
    c.setFont("Helvetica", 10)
    text = c.beginText()
    text.setTextOrigin(half_width + 2*cm, height - 8.5*cm)
    text.setLeading(24)
    c.setFillColor(HexColor("#3E2723"))

    for line in message.split("\n"):
        text.textLine(line)

    c.drawText(text)

    # ───────────── BACK PANEL (OPTIONAL) ─────────────
    c.setFont("Helvetica-Oblique", 12)
    c.setFillColor(HexColor("#8D6E63"))
    c.drawCentredString(
        half_width / 2,
        3*cm,
        "Made with ❤️"
    )

    # ✂️ Fold guide (light dashed line, printer-friendly)
    c.setStrokeColor(HexColor("#CCCCCC"))
    c.setDash(4, 4)
    c.line(half_width, 1*cm, half_width, height - 1*cm)

    c.showPage()
    c.save()
    buffer.seek(0)

    return buffer

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
    # 📄 Export PDF
        st.divider()

        pdf_buffer = generate_birthday_pdf(name, age, message)

        st.download_button(
            label="📄 Download Birthday Card (PDF)",
            data=pdf_buffer,
            file_name=f"birthday_card_{name}.pdf",
            mime="application/pdf"
        )


# ---------- Footer ----------
st.caption("Made with ❤️ using Streamlit")
