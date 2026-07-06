from pathlib import Path
from app.services.scan.scan_service import ScanService
from app.services.document.loader import DocumentLoader
from app.services.document.processor import DocumentProcessor

scan_service = ScanService()

file_path = Path("../sample_contracts/test_contract.txt")

document, findings = scan_service.scan(file_path)

print("File exists:", file_path.exists())
print("Absolute path:", file_path.resolve())

documents = DocumentLoader.load(file_path)

print("Number of documents:", len(documents))

for i, doc in enumerate(documents):
    print(f"\nDocument {i + 1}")
    print(repr(doc.page_content))

# document = DocumentProcessor.process(file_path)

print("\nProcessed Document")
print(document.model_dump_json(indent = 4))

from app.rules.rule_engine import RuleEngine

rule_engine = RuleEngine()

# findings = rule_engine.scan(document)

print("\nDetected Findings")

for finding in findings:
    print(finding.model_dump())