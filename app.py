import streamlit as st
import google.generativeai as genai

# Setup Configuration
st.set_page_config(page_title="Socrates: Pedagogical Knowledge Orchestrator", layout="wide")

# Ensure API Key is handled safely
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception:
    st.error("API Key not found. Please add GOOGLE_API_KEY to Streamlit Secrets.")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🏛️ Socrates Workbench")
module = st.sidebar.radio("Navigate Modules", [
    "Tutor (Persona-Adaptive)", 
    "Research Gap Identifier", 
    "Literature Review Finder", 
    "Pedagogical Roadmap",
    "NPTEL Transcoding Engine",
    "Philosophy and Epistemology", # Updated Name
    "Discovery Pathway"
])

# --- MAIN CONTENT AREA ---
st.title("Socrates: Agentic Pedagogical Knowledge Orchestrator")

# [Modules 1-5 remain consistent with previous iterations]
if module == "Philosophy and Epistemology":
    st.header("Philosophy and Epistemology: Cross-Tradition Synthesis")

    # 1. Disciplinary Philosophies
    with st.expander("1. Foundational Philosophies by Discipline"):
        phi_map = {
            "Philosophy of CS": "Ontological status of algorithms and logic.",
            "Philosophy of EEE": "Teleology of control, stability, and system feedback.",
            "Philosophy of ECE": "Information theory, signal propagation, and physical reality.",
            "Philosophy of Mathematics": "Platonism vs. Formalism; foundations of proof.",
            "Philosophy of Physics": "Determinism, quantum indeterminacy, and field theories.",
            "Philosophy of Mechanical Engg": "Mechanistic determinism and thermodynamics."
        }
        selection = st.selectbox("Select Discipline", list(phi_map.keys()))
        st.write(phi_map[selection])

    # 2. Philosophical Traditions to STEM
    with st.expander("2. Ancient Indian Philosophy to STEM"):
        st.write("**Nyāya-Vaiśeṣika:** Uses 5-step syllogism for AI inference.")
        st.write("**Pramāṇa:** Theory of valid knowledge (Perception, Inference, Testimony).")
        st.write("**Computational Linguistics:** Applying Pāṇini's Aṣṭādhyāyī to formal grammar[cite: 1].")

    with st.expander("3. Chinese Philosophy to STEM"):
        st.write("**Lǐ and Qì:** Principle (geometry/form) and Matter-energy flow[cite: 1].")
        st.write("**Wú Wéi:** Framework for autonomous, non-aggressive AI optimization[cite: 1].")
        st.write("**Yīn / Yáng:** Foundation for binary, control systems, and dualistic math[cite: 1].")

    with st.expander("4. Russian Philosophy to STEM"):
        st.write("**Kosmizm:** Planetary engineering and AI as part of a whole[cite: 1].")
        st.write("**Vseedinstvo (All-Unity):** Networked systems and distributed computing[cite: 1].")
        st.write("**Sophiology:** Structural knowledge and limits of mathematical representation[cite: 1].")

    with st.expander("5. Greek Philosophy to STEM"):
        st.write("**Socratic Method:** Dialectical inquiry for debugging and AI alignment.")
        st.write("**Aristotelian Logic:** Foundation of computational syllogism.")
        st.write("**Platonic Forms:** Ideal structures for abstract modeling in math/physics.")

    with st.expander("6. Japanese Philosophy to STEM"):
        st.write("**Ma (Negative Space):** Interval physics and signal processing[cite: 1].")
        st.write("**Mono no Aware:** Modeling limits and impermanence in AI lifecycle[cite: 1].")
        st.write("**Wabi-Sabi:** Heuristic approximations and fault-tolerant systems[cite: 1].")
        st.write("**Shuhari:** Mastery stages for machine learning systems[cite: 1].")

    # 3. University Programs
    with st.expander("7. Universities Teaching Philosophy of STEM"):
        st.write("- **MIT (USA):** Philosophy of Physics & AI Ethics.")
        st.write("- **Oxford (UK):** Philosophy of Mathematics & CS.")
        st.write("- **IIT Bombay (India):** Philosophy of Science & Logic.")
        st.write("- **Tsinghua University (China):** Philosophy of Technology.")
        st.write("- **University of Tokyo (Japan):** Philosophy of Robotics & Engineering.")
