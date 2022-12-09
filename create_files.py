from pathlib import Path
folder = Path.home() / "my_folder"
folder.mkdir(exist_ok=True)

new_files = [
    folder / "file1.txt",
    folder / "file2.txt",
    folder / "image1.png"
]
for files in new_files:
    files.touch(exist_ok=True)

images = folder / "images"
images.mkdir(exist_ok=True)

source = folder / "image1.png"
destination = images/ "image1.png"

source.replace(destination)
delete = folder/ "file1.txt"
delete.unlink()

delete = folder/images/"images1.png"

for files in delete:
    files.unlink()

deleteimagesfolder = folder / "images"
deleteimagesfolder.rmdir()