from pathlib import Path

directory = Path(__file__).parent
file_path = directory / "output.txt"

print(file_path)
