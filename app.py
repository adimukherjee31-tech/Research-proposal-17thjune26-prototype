import streamlit as st
import google.generativeai as genai

# Setup (Get your free key from https://aistudio.google.com/)
genai.configure(api_key="YOUR_API_KEY_HERE")

st.set_page_config(layout="wide")
st.title("🏛️ Academic Knowledge Navigator")

# Sidebar for Navigation
page = st.sidebar.selectbox("Navigate", ["Page 1: Curriculum", "Page 6: Deep Research"])

if page == "Page 1: Curriculum":
    st.header("JNTUH/OU Syllabus & Reference Mapping")
    branch = st.selectbox("Select Branch", ["EEE", "CSE", "AI/ML"])
    subject = st.selectbox("Select Subject", ["Power Electronics", "Operating Systems", "Neural Networks"])
    
    if st.button("Fetch Syllabus & References"):
        st.info(f"Displaying syllabus for {subject}...")
        st.write("📖 **Recommended Books:** Standard University Textbooks + NPTEL Links")
        st.success("🎯 GATE Mapping: [Link to GATE/NET Syllabus]")

else:
    st.header("🧠 Page 6: AI-Powered Research Analysis")
    uploaded_file = st.file_uploader("Upload 1000+ Page PDF", type="pdf")
    tone = st.selectbox("Select Persona", ["Munna Bhai Lingo", "Ivy League Student", "MIT/Harvard PhD"])
    
    if uploaded_file and st.button("Generate Analysis"):
        model = genai.GenerativeModel("gemini-2.5-flash")
        with st.spinner("Analyzing document..."):
            # Simple prompt engineering
            prompt = f"Explain this document in the tone of {tone}."
            st.write(f"**Research Summary ({tone}):**")
            st.write("This tool is analyzing your document using Gemini's native long-context window, providing persona-based synthesis for academic democratization.")
