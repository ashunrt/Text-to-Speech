import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
import os

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
    # Create TTS object and save as mp3
    myobj = gTTS(text=text, lang='en', tld='co.in', slow=False)
    output_path = "gtts_output/audio.mp3"
    myobj.save(output_path)

    # Speed up the audio
    if myobj:
        sound = AudioSegment.from_file(output_path)
        if sound:
            sound = sound.speedup(playback_speed=speed)  # Apply speed adjustment
            speed_up_path = "gtts_output/speed_up.mp3"
            sound.export(speed_up_path, format="mp3")

            # Provide download button for the modified audio file
            with open(speed_up_path, "rb") as audio_file:
                st.download_button(
                    label="Download",
                    data=audio_file,
                    file_name=file_name,  # Use the user-provided filename here
                    mime="audio/mp3"
                )
            if os.path.exists(output_path):
                os.remove(output_path)
            if os.path.exists(speed_up_path):
                os.remove(speed_up_path)
        else:
            st.write("Cannot access the mp3.")

