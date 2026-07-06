from pathlib import Path

from app.schemas.document import ExtractedDocument
from app.services.document.cleaner import TextCleaner
from app.services.document.loader import DocumentLoader
from app.services.document.splitter import DocumentSplitter

class DocumentProcessor:
    @staticmethod
    def process(file_path: Path) -> ExtractedDocument:
        documents = DocumentLoader.load(file_path)
        
        raw_text = "\n".join(
            document.page_content
            for document in documents
        )
        
        cleaned_text = TextCleaner.clean(documents)
        
        clauses = DocumentSplitter.split(cleaned_text)
        
        return ExtractedDocument(
            filename = file_path.name,
            raw_text= raw_text,
            cleaned_text = cleaned_text,
            clauses = clauses,
        )
        