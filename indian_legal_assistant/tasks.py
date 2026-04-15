from crewai import Task

class LegalTasks:
    def extraction_task(self, agent, document_content):
        return Task(
            description=f"""Extract the following information from the provided document:
            1. Parties involved (Accused, Complainant, Victim).
            2. Key dates and timeline of events.
            3. Specific sections of law mentioned (e.g., IPC/BNS sections).
            4. Summary of the primary allegations.

            Document Content: {document_content[:2000]}...""",
            expected_output="A structured report containing parties, timeline, legal sections, and fact summary.",
            agent=agent
        )

    def research_task(self, agent):
        return Task(
            description="""Research the legal implications of the extracted facts.
            Compare the mentioned IPC sections with their new BNS counterparts if applicable.
            Identify relevant Supreme Court precedents that could support a defense or prosecution based on these facts.""",
            expected_output="A legal research memorandum with statute comparisons and case law citations.",
            agent=agent
        )

    def audit_task(self, agent):
        return Task(
            description="""Analyze the case for any fatal procedural defects.
            Check for:
            - Delays in lodging the FIR.
            - Ambiguity in witness statements.
            - Missing procedural requirements (e.g., Section 161 CrPC/Section 180 BNSS statements).
            - Electronic evidence without proper certification.""",
            expected_output="A list of identified procedural gaps and potential grounds for quashing or bail.",
            agent=agent
        )

    def final_report_task(self, agent, context):
        return Task(
            description="""Consolidate all findings into a final, professional 'Legal Strategy Report' for a senior advocate.
            The report should be structured, concise, and highlight the strongest legal arguments.""",
            expected_output="A comprehensive 3-page style PDF-ready text report with sections: Case Summary, Legal Analysis, Procedural Gaps, and Strategic Recommendations.",
            agent=agent,
            context=context
        )
