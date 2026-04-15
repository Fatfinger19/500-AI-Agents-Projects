import streamlit as st
import os
import tempfile
from main import run_assistant
from tools import LegalTools

# Page Config
st.set_page_config(
    page_title="Nyaya AI | Legal Document Review Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS for Professional Lawyer Documents Design
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stApp {
        background-color: #ffffff;
        border-top: 10px solid #2c3e50;
    }
    .report-container {
        font-family: 'Times New Roman', serif;
        padding: 40px;
        background-color: white;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        border: 1px solid #ddd;
        line-height: 1.6;
    }
    .report-header {
        text-align: center;
        border-bottom: 2px solid #2c3e50;
        margin-bottom: 30px;
        padding-bottom: 10px;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/ffffff/scales.png", width=100)
    st.title("Nyaya AI")
    st.markdown("---")
    st.info("AI-powered Legal Review Assistant for the Indian Judicial System.")

    openai_key = st.text_input("OpenAI API Key", type="password", placeholder="sk-...")
    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key

    st.markdown("---")
    st.write("### Instructions")
    st.write("1. Upload a PDF or paste document text.")
    st.write("2. Provide your API key.")
    st.write("3. Click 'Analyze Document'.")

# Main UI
st.title("⚖️ Indian Legal Document Review Assistant")
st.markdown("### Professional Review & Strategy Generation")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📁 Input Document")
    input_method = st.radio("Choose Input Method", ["Upload PDF", "Paste Text"])

    doc_content = ""
    pdf_path = None

    if input_method == "Upload PDF":
        uploaded_file = st.file_uploader("Upload Legal Document (PDF)", type=["pdf"])
        if uploaded_file:
            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.getvalue())
                pdf_path = tmp.name
            st.success(f"File '{uploaded_file.name}' uploaded successfully.")

            # Show preview
            if st.button("Preview PDF Text"):
                text = LegalTools.pdf_search_tool.invoke(pdf_path)
                st.text_area("PDF Content Preview", text, height=200)

    else:
        doc_content = st.text_area("Paste Legal Document Text (FIR, Petition, etc.)", height=300, placeholder="Enter text here...")

with col2:
    st.subheader("🔍 Analysis Configuration")
    st.write("Agents in loop:")
    st.markdown("- **Legal Document Analyst**: Fact Extraction")
    st.markdown("- **Indian Law Expert**: Statute Mapping (IPC -> BNS)")
    st.markdown("- **Procedural Auditor**: Compliance Check")

    if st.button("🚀 Analyze Document", type="primary"):
        if not os.getenv("OPENAI_API_KEY"):
            st.error("Please provide an OpenAI API Key in the sidebar.")
        elif not (doc_content or pdf_path):
            st.error("Please provide document content or upload a PDF.")
        else:
            with st.spinner("⚖️ Nyaya AI is analyzing the case... this may take a minute."):
                try:
                    # Run the assistant
                    result = run_assistant(document_content=doc_content, pdf_path=pdf_path)

                    st.session_state['analysis_result'] = result
                    st.success("Analysis Complete!")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

# Display Result
if 'analysis_result' in st.session_state:
    st.markdown("---")
    st.header("📄 Legal Strategy Report")

    # Paper-like container for the report
    st.markdown('<div class="report-container">', unsafe_allow_html=True)

    st.markdown('<div class="report-header">', unsafe_allow_html=True)
    st.markdown("## NYAYA AI: LEGAL STRATEGY MEMORANDUM")
    st.markdown("#### CONFIDENTIAL | ATTORNEY-CLIENT PRIVILEGE")
    st.markdown('</div>', unsafe_allow_html=True)

    # Display the result
    st.markdown(st.session_state['analysis_result'])

    st.markdown('</div>', unsafe_allow_html=True)

    # Download option
    st.download_button(
        label="📥 Download Report (TXT)",
        data=str(st.session_state['analysis_result']),
        file_name="legal_strategy_report.txt",
        mime="text/plain"
    )

st.markdown("---")
st.caption("Developed for Indian Legal Market | BNS & BNSS Compliance Enabled")
