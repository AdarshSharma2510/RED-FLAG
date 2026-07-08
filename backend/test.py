from pathlib import Path

from app.services.scan.scan_service import ScanService
from app.ai.detector import GeminiDetector

# -------------------------------------------------------
# Test File
# -------------------------------------------------------

file_path = Path("../sample_contracts/test_contract.txt")

print("File exists:", file_path.exists())
print("Absolute path:", file_path.resolve())

# -------------------------------------------------------
# Existing Scan Pipeline
# -------------------------------------------------------

scan_service = ScanService()

response = scan_service.scan(file_path)

print("\n==================== SCAN RESPONSE ====================\n")

print(response.model_dump_json(indent=4))

# -------------------------------------------------------
# AI Detector (Standalone Test)
# -------------------------------------------------------

document = response.document

detector = GeminiDetector()

ai_findings = detector.detect(document)

print("\n==================== AI DETECTOR ====================\n")

print(ai_findings.model_dump_json(indent=4))