from PIL import Image
from sys import argv


def process_image(image : Image.Image) -> Image.Image:
    width, height = image.size
    bufferImage = Image.new("RGB", image.size)
    resultImage = Image.new("RGB", (width*4, height))
    data = image.getdata()
    resultImage.paste(image)

    for colorIndex in range(3):
        colorData = [tuple_color_masked(color, colorIndex) for color in data]
        bufferImage.putdata(colorData)
        resultImage.paste(bufferImage, (width * (1 + colorIndex), 0))
    return resultImage


def tuple_color_masked(originalColor : tuple[int, int, int], maskIndex : int) -> tuple[int, int, int]:
    r = originalColor[0] if maskIndex == 0 else 0
    g = originalColor[1] if maskIndex == 1 else 0
    b = originalColor[2] if maskIndex == 2 else 0

    return (r, g, b)

if(len(argv) < 2):
    print("You should specify filepath")
    exit()

filePath = argv[1]

with Image.open(filePath) as image:
   process_image(image).show()