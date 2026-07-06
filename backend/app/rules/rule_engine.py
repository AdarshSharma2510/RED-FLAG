from app.rules.legal_rules import LEGAL_RULES
from app.schemas.document import ExtractedDocument
from app.schemas.finding import RiskFinding
from app.schemas.enums import TriggerSource


class RuleEngine:
    def __init__(self):
        self.rules = LEGAL_RULES

    def scan(self, document: ExtractedDocument) -> list[RiskFinding]:
        findings: list[RiskFinding] = []

        for clause in document.clauses:
            for sentence in clause.sentences:
                sentence_text = sentence.text.lower()

                for rule in self.rules:
                    for pattern in rule.patterns:
                        if pattern.lower() in sentence_text:
                            findings.append(
                                RiskFinding(
                                    clause_id=clause.clause_id,
                                    sentence_id=sentence.sentence_id,
                                    clause_text= clause.text,
                                    matched_text=sentence.text,
                                    category=rule.category,
                                    severity=rule.severity,
                                    explanation=rule.explanation,
                                    trigger_source=TriggerSource.RULE_ENGINE,
                                )
                            )

        return findings