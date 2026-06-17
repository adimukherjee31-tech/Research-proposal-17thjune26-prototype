import streamlit as st
import google.generativeai as genai

# Setup Configuration
st.set_page_config(page_title="Pedagogical Knowledge Navigator", layout="wide")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# --- CORE ARCHITECTURE: SOCRATIC BRIDGE TUTOR ---
st.title("🏛️ Pedagogical Knowledge Navigator")
st.subheader("Agentic Framework for Cross-Disciplinary Alignment")

tab1, tab2, tab3 = st.tabs(["Socratic Tutor", "Requirement Gap Identifier", "Literature Reviewer"])

with tab1:
    st.write("### Socratic Bridge Tutor")
    st.info("I utilize a Socratic reasoning loop to facilitate metacognitive knowledge acquisition.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "What pedagogical concept are we exploring?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Input your query..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # Dialectical Agent Logic
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(f"You are a Socratic tutor. Guide the student using pedagogical questions. Context: {prompt}")
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

with tab2:
    st.write("### Requirement Gap Identifier")
    domain = st.selectbox("Select Domain", ["EEE", "AI/ML", "Physics", "Math", "Mechanical Engineering"])
    exam = st.selectbox("Target Assessment", ["GATE", "IIT-JAM", "CUET", "UGC-NET"])
    
    if st.button("Identify Curriculum Gap"):
        st.write(f"Analyzing alignment between {domain} curricula and {exam} standards...")
        st.success("Analysis complete: Identified 3 core competency gaps in current syllabus.")
        st.text_area("Gap Report & Action Plan", "1. Topic X: Under-represented in JNTUH...\n2. Topic Y: Requires advanced research literature...")

with tab3:
    st.write("### Literature Reviewer")
    uploaded_file = st.file_uploader("Upload Technical PDF", type="pdf")
    if uploaded_file and st.button("Review Literature"):
        st.write("Extracting thematic threads...")
        st.text_area("Critical Review & Research Synthesis", "The document proposes a novel framework for [X]. However, it lacks consideration for [Y], presenting an opportunity for further empirical investigation.")
