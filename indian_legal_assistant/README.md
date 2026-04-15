# Indian Legal Document Review Assistant ⚖️🇮🇳

An AI-powered multi-agent system built with **CrewAI** to assist Indian lawyers in reviewing legal documents (FIRs, Petitions, Charge-sheets) with a focus on Indian statutes (IPC, BNS, CrPC, BNSS).

## 🌟 Features
- **Document Analysis**: Extracts parties, dates, and legal sections automatically.
- **Statute Comparison**: Automatically maps traditional IPC sections to the new **Bharatiya Nyaya Sanhita (BNS)**.
- **Procedural Audit**: Identifies "Fatal Procedural Defects" such as delay in FIR or lack of Section 65B (Evidence Act) certification for digital evidence.
- **Legal Strategy Report**: Generates a consolidated report for senior advocates.

## 🏗️ Architecture
The system uses three specialized agents:
1. **Legal Document Analyst**: Handles fact extraction.
2. **Indian Law Expert**: Researches statutes and precedents.
3. **Procedural Auditor**: Scans for technical/procedural gaps.

## 🚀 Getting Started

### 1. Installation
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 2. Environment Setup
Create a `.env` file and add your OpenAI API key:
```env
OPENAI_API_KEY=your_key_here
```

### 3. Running the Assistant
You can run the main script to see a demonstration with a mock FIR:
```bash
python main.py
```

## 🛠️ Tools
- **PDF Search Tool**: Uses `pypdf` to parse legal documents.
- **Indian Law Lookup**: A specialized tool for querying Indian law (currently simulated).

## 📝 Disclaimer
This tool is intended for assistive purposes for legal professionals and does not constitute legal advice.
