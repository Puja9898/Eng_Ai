pip install streamlit
pip install googletrans==4.0.0-rc1
pip install SpeechRecognition
import streamlit as st
from googletrans import Translator

import speech_recognition as sr

def translate_text(text, src_lang, dest_lang="en"):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
        except sr.RequestError:
            st.error("Sorry, there was an issue with the speech recognition service.")
    return None

st.title("English Teaching AI")
input_method = st.radio("Choose input method:", ("Text", "Microphone"))

user_input = ""
if input_method == "Text":
    user_input = st.text_area("Enter text in your native language:")
else:
    if st.button("Start Recording"):
        user_input = speech_to_text()
        if user_input:
            st.write("You said:", user_input)

src_lang = st.selectbox("Select your native language:", ["hi",  # Hindi
            "te",  # Telugu
            "ta",  # Tamil
            "kn",  # Kannada
            "ml",  # Malayalam
            "mr",  # Marathi
            "bn",  # Bengali
            "gu",  # Gujarati
            "pa",  # Punjabi
            "ur",  # Urdu
            "es",  # Spanish
            "fr",  # French
            "de",  # German
            "zh-cn"])

if st.button("Translate to English"):
    if user_input:
        translated_text = translate_text(user_input, src_lang)
        st.write("Translated Text:", translated_text)
    else:
        st.warning("Please provide input text or use the microphone to speak.")
