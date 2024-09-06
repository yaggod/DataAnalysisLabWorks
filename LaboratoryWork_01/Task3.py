from sys import argv
from pathlib import Path
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--dirpath", type=str, default=str(Path(argv[0]).parent), help="Working directory path (default: current folder)") # that's not the same as path(".")
args = parser.parse_args()

filesToCreate = []
with Path(argv[0]).parent.joinpath("non-existing.txt").open() as inputFile:
    filesToCreate = inputFile.readlines()


directoryPath = Path(args.dirpath)
if(not directoryPath.exists()):
    directoryPath.mkdir()
    
for fileName in filesToCreate:
    try:
        filePath = directoryPath.joinpath(fileName.strip())
        filePath.touch()
    except FileExistsError:
        print(f"{fileName} already exists, skipping")

