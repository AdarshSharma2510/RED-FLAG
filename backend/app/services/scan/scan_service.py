from pathlib import Path
from app.rules.rule_engine import RuleEngine
from app.schemas.document import ExtractedDocument
from app.schemas.finding import RiskFinding
from app.services.document.processor import DocumentProcessor

class ScanService:
    def __init__(self):
        self.rule_engine = RuleEngine()

    def scan(self, file_path: Path) -> tuple[ExtractedDocument, list[RiskFinding]]:
        document = DocumentProcessor.process(file_path)
        
        findings = self.rule_engine.scan(document)
        
        return document, findings
    