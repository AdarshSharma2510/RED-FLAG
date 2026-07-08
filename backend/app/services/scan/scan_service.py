from pathlib import Path

from app.ai.detector import GeminiDetector
from app.rules.rule_engine import RuleEngine
from app.schemas.scan_response import ScanResponse
from app.schemas.scan_result import ScanResult
from app.services.ai.analysis_service import AnalysisService
from app.services.document.processor import DocumentProcessor
from app.services.scan.finding_merger import FindingMerger


class ScanService:
    def __init__(self):
        self.rule_engine = RuleEngine()
        self.detector = GeminiDetector()
        self.analysis_service = AnalysisService()

    def scan(self, file_path: Path) -> ScanResponse:
        # Process the uploaded document
        document = DocumentProcessor.process(file_path)

        # Rule-based detection
        rule_findings = self.rule_engine.scan(document)

        # AI-based detection
        ai_response = self.detector.detect(document)

        # Merge and deduplicate findings
        findings = FindingMerger.merge(
            document=document,
            rule_findings=rule_findings,
            ai_findings=ai_response.findings,
        )

        # Generate AI explanations
        analyses = self.analysis_service.analyze(findings)

        results = []

        for finding, analysis in zip(findings, analyses):
            results.append(
                ScanResult(
                    finding=finding,
                    analysis=analysis,
                )
            )

        return ScanResponse(
            document=document,
            results=results,
        )