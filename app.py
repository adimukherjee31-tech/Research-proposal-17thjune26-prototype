# Updated Tabs for Modular Research Workflow
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Tutor (Persona-Adaptive Synthesis)", 
    "Research Gap Identifier", 
    "Literature Review Finder", 
    "Pedagogical Roadmap",
    "NPTEL Asynchronous Pedagogical Transcoding Engine",
    "Philosophy & Epistemology" # New Section
])

# --- ADD THIS BLOCK FOR TAB 6 ---
with tab6:
    st.header("Philosophy & Epistemology: Foundational Inquiries")
    st.markdown("*A formal meta-analysis of core disciplinary axioms.*")
    
    phi_domain = st.selectbox("Select Foundational Inquiry", [
        "Philosophy of Computer Science", 
        "Philosophy of Physics", 
        "Philosophy of Mathematics", 
        "Philosophy of Electrical Engineering", 
        "Philosophy of Artificial Intelligence"
    ])
    
    # PhD-Level Dummy Data
    phi_data = {
        "Philosophy of Computer Science": "Focus on the ontological status of algorithms—are they mathematical objects or physical entities? Inquiry into Church-Turing thesis limits.",
        "Philosophy of Physics": "Exploration of the transition from classical determinism to quantum indeterminacy; investigation into the measurement problem and realism.",
        "Philosophy of Mathematics": "Examination of Platonism vs. Formalism; the epistemic access to abstract mathematical structures.",
        "Philosophy of Electrical Engineering": "Inquiry into the 'nature of control' and energy flow; the teleology of system stability and feedback loops.",
        "Philosophy of Artificial Intelligence": "Phenomenological critique of machine consciousness; the gap between syntactic processing and semantic understanding (Searle's Chinese Room)."
    }
    
    if st.button("Query Foundational Axioms"):
        st.info(f"### Meta-analysis of: {phi_domain}")
        st.write(phi_data[phi_domain])
        st.markdown("---")
        st.caption("Framework: Epistemic structural realism applied to disciplinary paradigms.")

# [Keep your existing tab1-tab5 blocks exactly as they were...]
