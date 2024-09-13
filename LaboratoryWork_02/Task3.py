from PIL import Image, ImageFile, ImageDraw
from pathlib import Path
from sys import argv


def get_copy_with_watermark(imageToModify : Image.Image, watermarkImage : Image.Image) -> Image.Image:
    newImage = imageToModify.convert("RGB")

    drawer = ImageDraw.Draw(newImage)
    drawer.bitmap((10, 10), watermarkImage, fill=(255, 0, 0)) 
    drawer.text((20, 35), "some text", fill=(255, 0, 0), align="center") # hardcoded but yea

    return newImage


if(len(argv) < 2):
    print("You should specify filepath")
    exit()
    
filePath =  Path(argv[1])
watermarkPath = Path(argv[0]).parent.joinpath("examplewatermark.png")
outputFile = filePath.parent.joinpath(filePath.stem + "_WATERMARKED.jpg")


with Image.open(filePath) as imageToModify, Image.open(watermarkPath) as watermarkImage:
    newImage = get_copy_with_watermark(imageToModify, watermarkImage)
    newImage.show()
    newImage.save(outputFile)