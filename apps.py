import streamlit as st
from googletrans import Translator
import speech_recognition as sr
import os

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    h1 {
        color: #1f77b4;
        text-align: center;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stTextArea textarea {
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 10px;
    }
    .stFileUploader div {
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 10px;
    }
    .stSelectbox div {
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 10px;
    }
    .stSuccess {
        color: #28a745;
    }
    .stWarning {
        color: #dc3545;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
    # App title
    st.markdown("<h1>🎤 English Teaching AI 🎓</h1>", unsafe_allow_html=True)

    # Input method selection
    st.markdown("### 📝 Choose Input Method")
    input_method = st.radio("", ("Text", "Audio File"), horizontal=True)

    # User input
    user_input = ""
    if input_method == "Text":
        st.markdown("### 📖 Enter Text")
        user_input = st.text_area("", placeholder="Type your text here...")
    else:
        st.markdown("### 🎧 Upload Audio File")
        audio_file = st.file_uploader("", type=["wav"])
        if audio_file:
            # Save the uploaded file temporarily
            with open("temp_audio.wav", "wb") as f:
                f.write(audio_file.getvalue())
            # Convert audio to text
            user_input = audio_to_text("temp_audio.wav")
            if user_input:
                st.markdown("### 🗣️ You Said:")
                st.write(user_input)
            # Clean up the temporary file
            os.remove("temp_audio.wav")

    # Language selection
    st.markdown("### 🌍 Select Your Native Language")
    src_lang = st.selectbox(
        "",
        [
              " Hindi"
              " Telugu"
              " Tamil"
              " Kannada
              " Malayalam
              " Marathi
              " Bengali
              " Gujarati
              " Punjabi
              " Urdu
              "Spanish
              " French
              " German
            "chinese",  
        ],
    )

    # Translate button
    st.markdown("### 🔄 Translate to English")
    if st.button("Translate"):
        if user_input:
            translated_text = translate_text(user_input, src_lang)
            st.markdown("### 🎉 Translated Text:")
            st.success(translated_text)
        else:
            st.warning("Please provide input text or upload an audio file.")

# Run the app
if __name__ == "__main__":
    main()
