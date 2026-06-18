import streamlit as st
import google.generativeai as genai

# 1. Page Config sabse upar
st.set_page_config(page_title="Socrates: Pedagogical Knowledge Orchestrator", layout="wide")

# 2. API Key setup
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("API Key not found.")

# 3. Header
st.title("🏛️ Socrates: Agentic Pedagogical Knowledge Orchestrator")

# 4. Yahan aayega tera Tabs definition (Ab error nahi aayega!)
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Tutor (Persona-Adaptive Synthesis)", 
    "Requirement Gap Identifier", 
    "Literature Review Finder", 
    "Pedagogical Roadmap",
    "NPTEL Asynchronous Pedagogical Transcoding Engine"
])

# Ab baaki ke 'with tabX:' blocks yahan neeche likho...
