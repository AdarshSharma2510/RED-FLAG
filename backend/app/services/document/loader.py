from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_core.documents import Document

class DocumentLoader:
    @staticmethod
    def load(file_path: Path)->list[Document]:
        suffix = file_path.suffix.lower()
        if suffix == ".txt":
            return TextLoader(str(file_path)).load()
    
        if suffix == ".pdf":
            return PyPDFLoader(str(file_path)).load()

        if suffix == ".docx":
            return Docx2txtLoader(str(file_path)).load()
        
        raise ValueError(f"Unsupported file type: {suffix}")