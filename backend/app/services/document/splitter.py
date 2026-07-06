import re

from app.schemas.document import Clause, Sentence


class DocumentSplitter:
    @staticmethod
    def split(text: str) -> list[Clause]:
        clause_texts = re.split(r"\n\s*\n", text)

        clauses: list[Clause] = []

        for clause_index, clause_text in enumerate(clause_texts, start=1):
            clause_text = clause_text.strip()

            if not clause_text:
                continue

            sentence_texts = re.split(r"(?<=[.!?])\s+", clause_text)
            
            sentences = [
                Sentence(
                    sentence_id=sentence_index,
                    text=sentence.strip(),
                )
                for sentence_index, sentence in enumerate(sentence_texts, start=1)
                if sentence.strip()
            ]
            clauses.append(
                Clause(
                    clause_id=clause_index,
                    text=clause_text,
                    sentences=sentences,
                )
            )
        return clauses
    