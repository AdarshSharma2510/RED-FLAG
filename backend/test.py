from pathlib import Path

from app.services.document.processor import DocumentProcessor

document = DocumentProcessor.process(
    Path("../sample_contracts/test_contract.txt")
)

print(document.model_dump())