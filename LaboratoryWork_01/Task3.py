from sys import argv
from pathlib import Path
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--dirpath", type=str, default="", help="Working directory path (default: current folder)") # that's not the same as path(".")
args = parser.parse_args()

filesToCreate = []
with Path(argv[0]).parent.joinpath("non-existing.txt").open() as inputFile: # that's actually not the same as open(fileName, "w")
    filesToCreate = inputFile.readlines()


directoryPath = Path(args.dirpath).mkdir(exist_ok=True)
    
for fileName in filesToCreate:
    try:
        filePath = directoryPath.joinpath(fileName.strip())
        filePath.touch()
    except FileExistsError:
        print(f"{fileName} already exists, skipping")

