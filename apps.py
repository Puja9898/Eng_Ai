import streamlit as st
from googletrans import Translator
import speech_recognition as sr
import os

# Custom CSS for modern styling with gradients and enhanced visuals
st.markdown(
    """
    <style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #EEF2FF 0%, #F5F3FF 100%);
        padding: 2rem;
    }
    
    /* Header styling */
    .stMarkdown h1 {
        background: linear-gradient(90deg, #2563EB 0%, #7C3AED 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem;
        font-size: 2.5rem;
        font-weight: bold;
    }
    
    /* Card-like container for content */
    .element-container {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 1rem;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    /* Input fields styling */
    .stTextArea textarea {
        border: 2px solid #BFDBFE;
        border-radius: 0.5rem;
        padding: 0.75rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #C4B5FD;
        box-shadow: 0 0 0 4px rgba(196, 181, 253, 0.2);
    }
    
    /* File uploader styling */
    .stFileUploader {
        border: 2px dashed #BFDBFE;
        border-radius: 0.5rem;
        padding: 1rem;
        text-align: center;
    }
    
    .stFileUploader:hover {
        border-color: #C4B5FD;
    }
    
    /* Select box styling */
    .stSelectbox {
        margin-bottom: 1rem;
    }
    
    .stSelectbox > div > div {
        border: 2px solid #BFDBFE;
        border-radius: 0.5rem;
        padding: 0.5rem;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #C4B5FD;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(90deg, #2563EB 0%, #7C3AED 100%);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 500;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Success/Warning message styling */
    .stSuccess {
        background: linear-gradient(90deg, #EFF6FF 0%, #F5F3FF 100%);
        border-left: 4px solid #7C3AED;
        padding: 1rem;
        border-radius: 0.5rem;
        color: #1F2937;
    }
    
    .stWarning {
        background: #FEF2F2;
        border-left: 4px solid #DC2626;
        padding: 1rem;
        border-radius: 0.5rem;
        color: #1F2937;
    }
    
    /* Radio button styling */
    .stRadio > div {
        background: #F3F4F6;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
    
    /* Tabs-like styling for radio buttons */
    .stRadio [role="radiogroup"] {
        display: flex;
        gap: 1rem;
        background: #F3F4F6;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
    
    .stRadio label {
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
        cursor: pointer;
    }
    
    .stRadio label:has(input:checked) {
        background: linear-gradient(90deg, #2563EB 0%, #7C3AED 100%);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError:
            st.error("Speech recognition service error.")
    return None

def main():
    # App title with emoji
    st.markdown("<h1>🌍 English Teaching AI ✨</h1>", unsafe_allow_html=True)
    
    # Language options
    languages = {
        "en": "English",
        "hi": "Hindi",
        "te": "Telugu",
        "ta": "Tamil",
        "kn": "Kannada",
        "ml": "Malayalam",
        "mr": "Marathi",
        "bn": "Bengali",
        "gu": "Gujarati",
        "pa": "Punjabi",
        "ur": "Urdu",
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "zh-cn": "Chinese (Simplified)"
    }
    
    # Input method selection with modern radio buttons
    st.markdown("### Choose Input Method")
    input_method = st.radio("", ("Text", "Audio"), horizontal=True)
    
    # User input section
    user_input = ""
    if input_method == "Text":
        st.markdown("### Enter Your Text")
        user_input = st.text_area("", placeholder="Type or paste your text here...", height=150)
    else:
        st.markdown("### Upload Audio File")
        audio_file = st.file_uploader("", type=["wav"])
        if audio_file:
            with open("temp_audio.wav", "wb") as f:
                f.write(audio_file.getvalue())
            user_input = audio_to_text("temp_audio.wav")
            if user_input:
                st.markdown("### Transcribed Text:")
                st.info(user_input)
            os.remove("temp_audio.wav")
    
    # Language selection
    st.markdown("### Select Languages")
    col1, col2 = st.columns(2)
    with col1:
        src_lang = st.selectbox("Source Language", options=list(languages.keys()), 
                               format_func=lambda x: languages[x])
    with col2:
        dest_lang = st.selectbox("Target Language", options=list(languages.keys()), 
                                format_func=lambda x: languages[x])
    
    # Translation button
    st.markdown("")  # Spacing
    if st.button("Translate"):
        if user_input:
            with st.spinner("Translating..."):
                translated_text = translate_text(user_input, src_lang, dest_lang)
                st.markdown("### Translation Result")
                st.success(translated_text)
        else:
            st.warning("Please provide input text or upload an audio file.")

if __name__ == "__main__":
    main()
