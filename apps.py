import streamlit as st
from googletrans import Translator
import speech_recognition as sr
import os

# Function to translate text
def translate_text(text, src_lang, dest_lang="en"):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

# Function to convert audio file to text
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
        except sr.RequestError:
            st.error("Sorry, there was an issue with the speech recognition service.")
    return None

# Streamlit app
def main():
    st.title("English Teaching AI 🎓")

    # Input method selection
    input_method = st.radio("Choose input method:", ("Text", "Audio File"))

    # User input
    user_input = ""
    if input_method == "Text":
        user_input = st.text_area("Enter text in your native language:")
    else:
        audio_file = st.file_uploader("Upload an audio file", type=["wav"])
        if audio_file:
            # Save the uploaded file temporarily
            with open("temp_audio.wav", "wb") as f:
                f.write(audio_file.getvalue())
            # Convert audio to text
            user_input = audio_to_text("temp_audio.wav")
            if user_input:
                st.write("You said:", user_input)
            # Clean up the temporary file
            os.remove("temp_audio.wav")

    # Language selection
    src_lang = st.selectbox(
        "Select your native language:",
        [
            "hindi",  # Hindi
            "telugu",  # Telugu
            "tamil",  # Tamil
            "kanada",  # Kannada
            "malayalam",  # Malayalam
            "marathi",  # Marathi
            "bengali",  # Bengali
            "gujarati",  # Gujarati
            "punjabi",  # Punjabi
            "urdu",  # Urdu
            "spanish",  # Spanish
            "french",  # French
            "german",  # German
            "chinese",  # Chinese (Simplified)
        ],
    )

    # Translate button
    if st.button("Translate to English"):
        if user_input:
            translated_text = translate_text(user_input, src_lang)
            st.success("Translated Text:")
            st.write(translated_text)
        else:
            st.warning("Please provide input text or upload an audio file.")

# Run the app
if __name__ == "__main__":
    main()
