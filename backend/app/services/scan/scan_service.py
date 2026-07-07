from pathlib import Path
from app.rules.rule_engine import RuleEngine
from app.schemas.document import ExtractedDocument
from app.schemas.finding import RiskFinding
from app.services.document.processor import DocumentProcessor
from app.services.ai.analysis_service import AnalysisService
from app.schemas.scan_result import ScanResult
from app.schemas.scan_response import ScanResponse

class ScanService:
    def __init__(self):
        self.rule_engine = RuleEngine()
        self.analysis_service = AnalysisService()

    def scan(self, file_path: Path) -> ScanResponse:
        document = DocumentProcessor.process(file_path)
        
        findings = self.rule_engine.scan(document)
        results: list[ScanResult] = []
        
        for finding in findings:
            analysis = self.analysis_service.analyze(finding)
            results.append(
                ScanResult(
                    finding=finding,
                    analysis=analysis,
                )
            )

        return ScanResponse(document = document, results = results)
            