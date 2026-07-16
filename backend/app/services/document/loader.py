from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
)
from langchain_core.documents import Document


class DocumentLoader:
    @staticmethod
    def load(file_path: Path) -> list[Document]:
        suffix = file_path.suffix.lower()

        if suffix == ".txt":
            # Try common text encodings in order
            for encoding in ("utf-8", "cp1252", "latin-1"):
                try:
                    text = file_path.read_text(encoding=encoding)
                    return [Document(page_content=text)]
                except UnicodeDecodeError:
                    continue

            raise ValueError(
                f"Unable to decode text file '{file_path.name}' with supported encodings."
            )

        elif suffix == ".pdf":
            return PyPDFLoader(str(file_path)).load()

        elif suffix == ".docx":
            return Docx2txtLoader(str(file_path)).load()

        raise ValueError(f"Unsupported file type: {suffix}")