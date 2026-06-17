import streamlit as st
import google.generativeai as genai

# Setup Configuration
st.set_page_config(page_title="Socrates: Pedagogical Knowledge Orchestrator", layout="wide")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# --- HEADER ---
st.title("🏛️ Socrates: Agentic Pedagogical Knowledge Orchestrator")
st.markdown("### *Systemic Analysis for Academic & Research Advancement*")

# Tabs for Modular Research Workflow
# Added "Research Gap Identifier" as the 4th tab
tab1, tab2, tab3, tab4 = st.tabs(["Socratic Tutor", "Requirement Gap Identifier", "Literature Reviewer", "Research Gap Identifier"])

with tab1:
    st.write("### Socratic Bridge Tutor")
    # ... (Your existing Socratic Tutor code) ...

with tab2:
    st.write("### Requirement Gap Identifier")
    # ... (Your existing Requirement Gap Identifier code) ...

with tab3:
    st.write("### Literature Reviewer")
    # ... (Your existing Literature Reviewer code) ...

with tab4:
    st.write("### Research Gap Identifier")
    st.info("Agentic analysis to identify unaddressed research frontiers.")
    
    research_topic = st.text_input("Enter the Research Topic (e.g., 'Genetic Algorithms in EEE')")
    
    if st.button("Identify Research Gaps"):
        with st.spinner("Analyzing current state-of-the-art..."):
            model = genai.GenerativeModel("gemini-2.0-flash")
            prompt = f"Act as an expert researcher. Identify significant research gaps and unexplored frontiers in: {research_topic}. Provide a critical analysis."
            response = model.generate_content(prompt)
            
            st.write("### Critical Gap Analysis")
            st.markdown(response.text)
            
            st.write("---")
            st.success("Analysis complete. These gaps represent high-potential research directions.")
