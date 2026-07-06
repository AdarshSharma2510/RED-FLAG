from langchain_core.prompts import ChatPromptTemplate

from app.schemas.finding import RiskFinding


class PromptBuilder:
    _template = ChatPromptTemplate.from_messages(
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

    @classmethod
    def build(cls, finding: RiskFinding):
        return cls._template.invoke(
            {
                "clause": finding.clause_text,
                "category": finding.category,
                "rule_explanation": finding.explanation,
            }
        )