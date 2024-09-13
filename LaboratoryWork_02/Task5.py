from PIL import Image, ImageDraw
from pathlib import Path
from argparse import ArgumentParser
from sys import argv

parser = ArgumentParser()
parser.add_argument("--ftype", type=str, default="png", help="Target files extension (default: png)")
args = parser.parse_args()


filesToShow = Path(".").glob(f"*.{args.ftype}")
for file in filesToShow:
    print(file)
    with Image.open(file) as image:
        image.resize((50, 50)).show()