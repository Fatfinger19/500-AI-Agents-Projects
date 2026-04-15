import os
from langchain.tools import tool
from pypdf import PdfReader

class LegalTools:

    @tool("pdf_search_tool")
    def pdf_search_tool(pdf_path: str):
        """Extracts text from a provided PDF file path."""
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

    @tool("indian_law_lookup")
    def indian_law_lookup(query: str):
        """Searches for Indian statutes (IPC, BNS, CrPC, BNSS) and Supreme Court precedents.
        Note: This is a simulated tool for demonstration.
        """
        # In a real project, this would interface with a legal API or Vector DB
        simulated_db = {
            "302 IPC": "Section 302 IPC deals with punishment for murder. Corresponding BNS section is 101.",
            "420 IPC": "Section 420 IPC deals with Cheating. Corresponding BNS section is 318.",
            "65B Evidence Act": "Requires a certificate for admissibility of electronic evidence. Corresponding BSA section is 63.",
            "delay in FIR": "Supreme Court in 'State of HP v. Gian Chand' held that unexplained delay in FIR can be fatal to prosecution.",
            "quashing": "Section 482 CrPC (now Section 528 BNSS) gives High Courts inherent powers to quash FIRs to prevent abuse of process."
        }

        for key, value in simulated_db.items():
            if key.lower() in query.lower():
                return value

        return "Legal reference found. Based on current Indian jurisprudence, the matter requires detailed examination of the specific facts against BNS/BNSS 2023 provisions."
