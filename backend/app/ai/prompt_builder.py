from langchain_core.prompts import ChatPromptTemplate

from app.schemas.document import ExtractedDocument
from app.schemas.finding import RiskFinding


class PromptBuilder:
    _explanation_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "You are an expert legal contract analyzer.\n"
                    "Your job is to explain why a legal clause may be risky.\n"
                    "Respond clearly and professionally."
                ),
            ),
            (
                "human",
                (
                    "Clause:\n"
                    "{clause}\n\n"
                    "Detected Category: {category}\n"
                    "Rule Explanation: {rule_explanation}\n\n"
                    "Explain:\n"
                    "1. Why this clause may be risky.\n"
                    "2. What legal consequences it could have.\n"
                    "3. Whether a user should negotiate this clause."
                ),
            ),
        ]
    )

    _detection_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "You are an expert legal contract reviewer.\n"
                    "Your task is to identify legal clauses that may expose a user "
                    "to legal, financial, privacy, or contractual risks.\n\n"
                    "Do NOT explain the risks in detail.\n"
                    "Only identify risky clauses.\n"
                    "Ignore clauses that appear safe.\n"
                    "Return every risky clause you identify.\n"
                    "Return only the findings using the required structured output.\n\n"
                    "Possible categories include:\n"
                    "- Automatic Renewal\n"
                    "- Data Sharing\n"
                    "- Termination\n"
                    "- Liability\n"
                    "- Indemnification\n"
                    "- Confidentiality\n"
                    "- Arbitration\n"
                    "- Jurisdiction\n"
                    "- Intellectual Property\n"
                    "- Non-Compete\n"
                    "- Exclusivity\n"
                    "- Limitation of Liability\n"
                    "- Assignment\n"
                    "- Payment Terms\n"
                    "- Refund Policy\n"
                    "- Warranty\n"
                    "- Force Majeure\n"
                    "- Governing Law\n\n"
                    "You may detect additional categories if appropriate."
                ),
            ),
            (
                "human",
                (
                    "Analyze the following contract.\n\n"
                    "Filename:\n"
                    "{filename}\n\n"
                    "Contract:\n"
                    "{contract}"
                ),
            ),
        ]
    )

    _batch_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "You are an expert legal contract analyzer.\n\n"
                    "For each finding provided, generate:\n"
                    "- risk_summary\n"
                    "- legal_consequence\n"
                    "- recommendation\n"
                    "- confidence (0.0 to 1.0)\n\n"
                    "Return ONLY the required structured output."
                ),
            ),
            (
                "human",
                (
                    "Analyze the following findings:\n\n"
                    "{findings}"
                ),
            ),
        ]
    )

    @classmethod
    def build(cls, finding: RiskFinding):
        return cls._explanation_template.invoke(
            {
                "clause": finding.clause_text,
                "category": finding.category,
                "rule_explanation": finding.explanation,
            }
        )

    @classmethod
    def build_detection(cls, document: ExtractedDocument):
        return cls._detection_template.invoke(
            {
                "filename": document.filename,
                "contract": document.cleaned_text,
            }
        )

    @classmethod
    def build_batch(cls, findings: list[RiskFinding]):
        findings_text = ""

        for i, finding in enumerate(findings, start=1):
            findings_text += (
                f"Finding {i}\n"
                f"Clause:\n{finding.clause_text}\n\n"
                f"Category: {finding.category}\n"
                f"Rule Explanation: {finding.explanation}\n\n"
            )

        return cls._batch_template.invoke(
            {
                "findings": findings_text,
            }
        )