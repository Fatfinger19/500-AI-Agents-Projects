import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import LegalAgents
from tasks import LegalTasks
from tools import LegalTools

# Load environment variables
load_dotenv()

def run_assistant(document_content=None, pdf_path=None):
    # Initialize Agents
    agents = LegalAgents()
    tasks = LegalTasks()

    analyst = agents.document_analyst()
    expert = agents.law_expert()
    auditor = agents.procedural_auditor()

    # Assign tools to agents
    analyst.tools = [LegalTools.pdf_search_tool]
    expert.tools = [LegalTools.indian_law_lookup]
    auditor.tools = [LegalTools.indian_law_lookup]

    # Use content from PDF if provided, otherwise use string content
    if pdf_path and not document_content:
        # In a real CrewAI flow, the agent would use the tool to read the PDF
        # We'll pass the path to the task description
        document_content = f"Please read and analyze the PDF file at: {pdf_path}"

    # Define Tasks
    extract_info = tasks.extraction_task(analyst, document_content)
    research_case = tasks.research_task(expert)
    audit_procedure = tasks.audit_task(auditor)

    # Final consolidated task
    final_report = tasks.final_report_task(
        expert,
        [extract_info, research_case, audit_procedure]
    )

    # Initialize Crew
    legal_crew = Crew(
        agents=[analyst, expert, auditor],
        tasks=[extract_info, research_case, audit_procedure, final_report],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = legal_crew.kickoff()
    return result

if __name__ == "__main__":
    # Sample Mock FIR Content for testing
    mock_fir = """
    FIRST INFORMATION REPORT (Under Section 154 Cr.P.C.)
    Police Station: Central Delhi, District: New Delhi
    FIR No: 0045/2024, Date: 15/08/2024

    1. Details of Complainant: Mr. Rajesh Kumar, S/o Late Shri Mohan Lal.
    2. Details of Accused: Mr. Vijay Mallya (Alias), Resident of Bangalore.
    3. Sections of Law: Section 420, 406, 120B of Indian Penal Code (IPC).
    4. Date & Time of Incident: 01/01/2023 to 31/12/2023.
    5. Date & Time of Reporting: 15/08/2024 (Delay of 8 months).

    Facts of the Case:
    The complainant alleges that the accused induced him to invest Rs. 50 Lakhs in a shell company with promises of 20% returns.
    The accused later disappeared and switched off his phone. Complainant provided WhatsApp screenshots as evidence.
    No Section 65B certificate was attached with the screenshots at the time of FIR.
    """

    print("### STARTING INDIAN LEGAL DOCUMENT REVIEW ASSISTANT ###")
    analysis_result = run_assistant(mock_fir)
    print("\n\n##############################")
    print("## FINAL LEGAL STRATEGY REPORT ##")
    print("##############################\n")
    print(analysis_result)
