from pathlib import Path
folder = Path.home() / "Practice files folder"
folder.mkdir(exist_ok=True)

sub_folder = folder / "documents"
sub_folder.mkdir(exist_ok=True)

sub_folder_files = [
    sub_folder / "text.txt",
    sub_folder / "meme.gif",
    sub_folder / "image1.png",
    sub_folder / "image2.gif",
    sub_folder / "image3.png",
    sub_folder / "image4.jpg"
]
for files in sub_folder_files:
    files.touch(exist_ok=True)

image_folder = folder / "images"
image_folder.mkdir(exist_ok=True)

file1 = sub_folder / "image1.png"
destination1 = sub_folder / "images1.png"
file1.replace(destination1)

file2 = sub_folder / "image2.gif"
destination2 = sub_folder / "images2.gif"
file2.replace(destination2)

file3 = sub_folder / "image3.png"
destination3 = sub_folder / "images3.png"
file3.replace(destination3)