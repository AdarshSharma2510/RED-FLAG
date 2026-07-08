from app.schemas.ai_detection import AIFinding
from app.schemas.document import ExtractedDocument
from app.schemas.enums import TriggerSource
from app.schemas.finding import RiskFinding


class FindingMerger:
    @staticmethod
    def merge(
        document: ExtractedDocument,
        rule_findings: list[RiskFinding],
        ai_findings: list[AIFinding],
    ) -> list[RiskFinding]:

        merged = list(rule_findings)

        existing = {
            (
                finding.clause_text.strip().lower(),
                finding.category.lower(),
            ): finding
            for finding in merged
        }

        for ai in ai_findings:
            key = (
                ai.clause_text.strip().lower(),
                ai.category.lower(),
            )

            # Already detected by Rule Engine
            if key in existing:
                existing[key].trigger_source = TriggerSource.BOTH
                continue

            clause_id = 0
            sentence_id = 0

            for clause in document.clauses:
                if clause.text.strip() == ai.clause_text.strip():
                    clause_id = clause.clause_id

                    for sentence in clause.sentences:
                        if sentence.text.strip() in ai.clause_text:
                            sentence_id = sentence.sentence_id
                            break

                    break

            new_finding = RiskFinding(
                clause_id=clause_id,
                sentence_id=sentence_id,
                clause_text=ai.clause_text,
                matched_text=ai.clause_text,
                category=ai.category,
                severity=ai.severity,
                explanation=ai.explanation,
                trigger_source=TriggerSource.LLM,
            )

            merged.append(new_finding)
            existing[key] = new_finding

        return merged