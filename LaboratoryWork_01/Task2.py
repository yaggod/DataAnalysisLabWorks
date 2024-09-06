from sys import argv
from pathlib import Path
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--dirpath", type=str, default=str(Path(argv[0]).parent))
parser.add_argument("--files", type=str, nargs="*", action="append")
args = parser.parse_args()


def output_and_print_list(fileName, list):
    with open(fileName, "w") as outputFile:
        for item in list:
            outputFile.write(item)
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
    
    return


if(args.files and len(args.files) > 0):
    process_files(args.dirpath, args.files[0]) # for some reasong args.files is a list containing another list
else:
    process_directory(args.dirpath)

