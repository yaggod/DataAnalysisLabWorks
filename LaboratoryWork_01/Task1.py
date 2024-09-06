from sys import argv
from pathlib import Path
from shutil import copy



expectedLength = 2048
if(len(argv) > 1 ):
    currentPath = Path(argv[1])
else:
    currentPath = Path(".")

allFoundItems = currentPath.glob("*")
validFiles = []

for item in allFoundItems:
    if(item.stat().st_size < expectedLength and item.is_file()):
        validFiles.append(item)

if(len(validFiles)):
    print("Found files:")
    newFolder = Path(".").joinpath("small")
    newFolder.mkdir(exist_ok=True)

    for file in validFiles:
        copy(file.absolute(), newFolder.joinpath(file.name))
        print(f"\t{file.absolute()}")

else:
    print(f"Files with size below {expectedLength} not found in {currentPath}")