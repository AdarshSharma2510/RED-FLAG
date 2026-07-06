import re

from app.schemas.document import Clause, Sentence


class DocumentSplitter:
    @staticmethod
    def split(text: str) -> list[Clause]:
        paragraphs = [
            paragraph.strip()
            for paragraph in re.split(r"\n\s*\n", text)
            if paragraph.strip()
        ]

        clauses: list[Clause] = []
        pending_title: str | None = None
        clause_id = 1

        for paragraph in paragraphs:
            is_heading = (
                "\n" not in paragraph
                and len(paragraph.split()) <= 8
                and not paragraph.endswith((".", "!", "?"))
            )

            if is_heading:
                pending_title = paragraph
                continue

            sentence_texts = re.split(r"(?<=[.!?])\s+", paragraph)

            sentences = [
                Sentence(
                    sentence_id=sentence_id,
                    text=sentence.strip(),
                )
                for sentence_id, sentence in enumerate(sentence_texts, start=1)
                if sentence.strip()
            ]

            clauses.append(
                Clause(
                    clause_id=clause_id,
                    title=pending_title,
                    text=paragraph,
                    sentences=sentences,
                )
            )

            clause_id += 1
            pending_title = None

        return clauses