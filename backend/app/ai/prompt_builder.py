from app.schemas.finding import RiskFinding


class PromptBuilder:
    @staticmethod
    def build(finding: RiskFinding) -> str:
        return f"""
You are a legal contract analysis assistant.

Analyze the following legal clause.

Category:
{finding.category}

Severity:
{finding.severity}

Rule Explanation:
{finding.explanation}

Clause:
{finding.clause_text}

Matched Sentence:
{finding.matched_text}

Your task:
1. Explain why this clause may be risky.
2. Explain the legal implications.
3. Mention if the rule engine appears correct or not. It may be wrong.
4. Respond professionally.
""".strip()