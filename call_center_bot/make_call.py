import streamlit as st
from gtts import gTTS
import os

# Define your scripted message
script = """
Jeki Panchal aapka haardik swagat karta hai evam abhinandan karta hai.
Kya aap Jeki Panchal se apna website develop karwana chahte hain?
Yadi haan toh 1 dabayein, warna call kat sakte hain.
"""

# Set up the Streamlit app
st.title("📞 Click to Play Scripted Message")

# Button to generate and play the audio
if st.button("▶️ Play Message"):
    tts = gTTS(text=script, lang='hi')
    tts.save("message.mp3")
    audio_file = open("message.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    audio_file.close()
    os.remove("message.mp3")
