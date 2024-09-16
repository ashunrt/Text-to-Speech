import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
import io

st.title("Text To Speech")
text = st.text_input("Text Input")

# Validate and set audio speed
try:
    speed = float(st.text_input("Audio Speed", "1.0"))
except ValueError:
    speed = 1.0
    st.error("Invalid speed value. Defaulting to 1.0")

# Set output filename
file_name = st.text_input("Output Filename", "example.mp3")
submit = st.button("Submit")

if submit and text:
    # Create TTS object and save as mp3 in memory
    myobj = gTTS(text=text, lang='en', tld='co.in', slow=False)

    # Save to BytesIO object instead of a file
    tts_audio = io.BytesIO()
    myobj.save(tts_audio)
    tts_audio.seek(0)  # Reset file pointer to start

    # Load TTS audio into pydub for processing (speed change)
    sound = AudioSegment.from_file(tts_audio, format="mp3")
    sound = sound.speedup(playback_speed=speed)

    # Save the sped-up audio to another BytesIO object
    sped_up_audio = io.BytesIO()
    sound.export(sped_up_audio, format="mp3")
    sped_up_audio.seek(0)

    # Provide download button for the modified audio file
    st.download_button(
        label="Download",
        data=sped_up_audio,
        file_name=file_name,
        mime="audio/mp3"
    )
