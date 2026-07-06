from pydantic import BaseModel

class Sentence(BaseModel):
    sentence_id: int
    text: str
    
class Clause(BaseModel):
    clause_id: int 
    section: str | None = None
    title: str | None = None
    text: str
    sentences: list[Sentence]
    
class ExtractedDocument(BaseModel):
    filename: str
    raw_text: str
    cleaned_text: str
    clauses: list[Clause]
