import streamlit as st
import google.generativeai as genai

# Setup
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"]) # Use Streamlit secrets for security

st.title("🎓 The Socratic Bridge Tutor")
st.subheader("I don't give answers; I help you find them.")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "What concept are you struggling with today?"}]

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Socratic Logic
if prompt := st.chat_input("Ask about any subject..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    model = genai.GenerativeModel("gemini-2.0-flash")
    # THE SOCRATIC PROMPT
    system_instruction = "You are a Socratic tutor. Never provide direct answers. Instead, ask probing questions that guide the student to the answer based on their JNTUH/OU curriculum."
    
    response = model.generate_content(f"{system_instruction}\nStudent says: {prompt}")
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
