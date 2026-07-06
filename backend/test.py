from pathlib import Path

from app.services.document.loader import DocumentLoader
from app.services.document.processor import DocumentProcessor

file_path = Path("../sample_contracts/test_contract.txt")

print("File exists:", file_path.exists())
print("Absolute path:", file_path.resolve())

documents = DocumentLoader.load(file_path)

print("Number of documents:", len(documents))

for i, doc in enumerate(documents):
    print(f"\nDocument {i + 1}")
    print(repr(doc.page_content))

document = DocumentProcessor.process(file_path)

print("\nProcessed Document")
print(document.model_dump())