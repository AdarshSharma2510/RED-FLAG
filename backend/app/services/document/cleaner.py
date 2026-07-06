import re
from langchain_core.documents import Document


class TextCleaner:
    @staticmethod
    def clean(documents: list[Document]) -> str:
        text = "\n".join(doc.page_content for doc in documents)
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()