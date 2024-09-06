from sys import argv
from pathlib import Path
from argparse import ArgumentParser




def output_and_print_list(fileName, list):
    with Path(argv[0]).parent.joinpath(fileName).open("w") as outputFile: # that's actually not the same as open(fileName, "w")
        for item in list:
            outputFile.write(item + "\n")
            print(item)

def process_files(directory, filesNames):
    existingFiles = []
    nonExistingFiles = []

    currentDirectory = Path(directory)
    for fileName in filesNames:
        currentFile = currentDirectory.joinpath(fileName)
        if(currentFile.exists()):
            existingFiles.append(fileName)
        else:
            nonExistingFiles.append(fileName)
    print("Existing files: ")
    output_and_print_list("existing.txt", existingFiles)
    print("Non-existing files: ")
    output_and_print_list("non-existing.txt", nonExistingFiles)

def process_directory(directory):
    print(f"Files found in {directory}: ")
    currentDirectory = Path(directory)
    totalSize = 0
    for item in currentDirectory.glob("*"):
        if(item.is_file()):
            totalSize += item.stat().st_size
            print(item.name)
    print(f"Total files size: {totalSize}")
    
            
parser = ArgumentParser()
parser.add_argument("--dirpath", type=str, default=str(Path(argv[0]).parent))
parser.add_argument("--files", type=str, nargs="*", action="append")
args = parser.parse_args()

if(args.files and len(args.files) > 0):
    process_files(args.dirpath, args.files[0]) # for some reasong args.files is a list containing another list
else:
    process_directory(args.dirpath)

