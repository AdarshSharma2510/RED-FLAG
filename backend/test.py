from pathlib import Path

from app.services.scan.scan_service import ScanService

scan_service = ScanService()

file_path = Path("../sample_contracts/test_contract.txt")

print("File exists:", file_path.exists())
print("Absolute path:", file_path.resolve())

response = scan_service.scan(file_path)

print("\n==================== SCAN RESPONSE ====================\n")

print(response.model_dump_json(indent=4))