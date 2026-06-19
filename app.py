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
    "Philosophy & Epistemology",
    "Discovery Pathway" # New Module
])

# --- MAIN CONTENT AREA ---
st.title("Socrates: Agentic Pedagogical Knowledge Orchestrator")

# ... [Modules 1-6 remain unchanged] ...

elif module == "Discovery Pathway":
    st.header("Discovery Pathway: Inquiry, Critical Thinking & Computational Skills")
    st.markdown("""
    To boost inquiry, critical thinking, and computational thinking in STEM fields, start by training your mind to ask **"Why?"** (Inquiry), analyze **"Is this the best way?"** (Critical thinking), and **"How can I break this down into algorithms?"** (Computational thinking)[cite: 1].
    
    The best way to master these interdisciplinary fields is through project-based learning.
    """)
    
    # Discovery Pathway Data
    pathway_data = {
        "EEE": {
            "Problem": "Designing power grids or circuits.",
            "Inquiry": "Why do transformers waste so much energy as heat, and how can we minimize it?",
            "Computational Thinking": "Decompose the circuit into logical stages (input, amplification, output). Use abstraction by representing complex transistors as logic gates.",
            "Critical Thinking": "Evaluate whether physical limitations (e.g., thermal limits) can be solved by better materials or smarter layouts.",
            "Examples": "Building a custom IoT solar charge controller; Designing a PCB that filters high-frequency audio noise."
        },
        "AI": {
            "Problem": "Teaching machines to mimic human intelligence.",
            "Inquiry": "How do natural language models determine context without possessing actual consciousness?",
            "Computational Thinking": "Create step-by-step algorithms for data extraction. Break down unstructured raw text into manageable tokens.",
            "Critical Thinking": "Question data sources for inherent bias. Test model limitations in handling edge cases.",
            "Examples": "Building a localized chatbot for college admissions; Designing an AI system that flags fake news using classification algorithms."
        },
        "Machine Learning": {
            "Problem": "Using statistical models to make predictions from data.",
            "Inquiry": "How can historical patterns in energy consumption predict future load?",
            "Computational Thinking": "Identify patterns in large datasets. Design pipelines to clean, normalize, and split data.",
            "Critical Thinking": "Evaluate which algorithm (e.g., Random Forest vs. Neural Network) is best, ensuring the model doesn't overfit.",
            "Examples": "Predicting electricity consumption using TensorFlow; Developing predictive maintenance for industrial machines."
        },
        "Interdisciplinary (EEE + AI + ML)": {
            "Problem": "Smart Grid Optimization & Computer Vision.",
            "Inquiry": "How can the grid learn to route power away from unused sectors automatically?",
            "Computational Thinking": "Decompose image analysis into pixel arrays (abstraction) to feed into an ML model.",
            "Critical Thinking": "Evaluate how latency in EEE hardware sensors affects the ML algorithm's ability to navigate safely.",
            "Examples": "Smart meters with time-series forecasting; CNNs for identifying flawed soldering on PCBs."
        }
    }
    
    selected_domain = st.selectbox("Select Domain for Discovery", list(pathway_data.keys()))
    data = pathway_data[selected_domain]
    
    st.subheader(f"Focus: {selected_domain}")
    st.write(f"**The Problem:** {data['Problem']}")
    st.write(f"**Inquiry:** {data['Inquiry']}")
    st.write(f"**Computational Thinking:** {data['Computational Thinking']}")
    st.write(f"**Critical Thinking:** {data['Critical Thinking']}")
    st.write(f"**Examples:** {data['Examples']}")

    st.markdown("---")
    st.markdown("### How to get started:")
    st.markdown("* **Learn by building**: Start with beginner-friendly projects.")
    st.markdown("* **Train your brain**: Practice the 4 pillars of computational thinking (Decomposition, Pattern Recognition, Abstraction, Algorithms).")
