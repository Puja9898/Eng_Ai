import streamlit as st
from googletrans import Translator
import speech_recognition as sr

# Function to translate text
def translate_text(text, src_lang, dest_lang="en"):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

# Streamlit app
def main():
    st.title("English Teaching AI 🎓")

    # Input method selection
    input_method = st.radio("Choose input method:", ("Text", "Microphone"))

    # User input
    user_input = ""
    if input_method == "Text":
        user_input = st.text_area("Enter text in your native language:")
    else:
        st.warning("Microphone input is not supported in this environment. Please use text input.")

    # Language selection
    src_lang = st.selectbox(
        "Select your native language:",
        [
            "hi",  # Hindi
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
            "zh-cn",  # Chinese (Simplified)
        ],
    )

    # Translate button
    if st.button("Translate to English"):
        if user_input:
            translated_text = translate_text(user_input, src_lang)
            st.success("Translated Text:")
            st.write(translated_text)
        else:
            st.warning("Please provide input text.")

# Run the app
if _name_ == "_main_":
    main()
