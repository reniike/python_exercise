import pathlib
from pathlib import Path

path = Path("C:/my_folder")
path.mkdir(exist_ok=True)
file_path = path / "my_file.txt"
file_path.touch()

print(file_path.exists())
print(file_path.name)
print(file_path.parent.name)



