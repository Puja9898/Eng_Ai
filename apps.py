import streamlit as st
from googletrans import Translator
import speech_recognition as sr
import os

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: "black";
    }
    .title {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #ffffff;
    }
    .button {
        background-color: #28a745 !important;
        color: white !important;
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
    }
    .success {
        color: #17a2b8;
        font-size: 18px;
        font-weight: bold;
    }
    .warning {
        color: #ffc107;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to translate text
def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

# Function to convert audio file to text
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError:
            st.error("Speech recognition service error.")
    return None

# Streamlit app
def main():
    st.markdown("<h1 class='title'>🎤 English Teaching AI 🎓</h1>", unsafe_allow_html=True)
    
    # Sidebar for language selection
    st.sidebar.header("🌍 Language Selection")
    src_lang = st.sidebar.selectbox("Source Language", [
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
], index=0)
    dest_lang = st.sidebar.selectbox("Target Language", [
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
], index=1)

    # Input method selection
    st.markdown("### 📝 Choose Input Method")
    input_method = st.radio("Select Input Method", ("Text", "Audio File"), horizontal=True)
    
    user_input = ""
    if input_method == "Text":
        user_input = st.text_area("Enter Text", placeholder="Type your text here...")
    else:
        audio_file = st.file_uploader("Upload Audio File", type=["wav"])
        if audio_file:
            with open("temp_audio.wav", "wb") as f:
                f.write(audio_file.getvalue())
            user_input = audio_to_text("temp_audio.wav")
            if user_input:
                st.markdown("### 🗣️ Detected Speech:")
                st.write(user_input)
            os.remove("temp_audio.wav")
    
    # Translate button
    if st.button("Translate", key="translate_button", help="Click to translate the text/audio"):
        if user_input:
            translated_text = translate_text(user_input, src_lang, dest_lang)
            st.markdown("### 🎉 Translated Text:")
            st.success(translated_text)
        else:
            st.warning("Please provide input text or upload an audio file.")

if __name__ == "__main__":
    main()
