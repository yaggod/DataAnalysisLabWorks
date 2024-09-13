from PIL import Image
from sys import argv


def get_total_colors_weights(image : Image.Image) -> list[int]:
    data = image.getdata()

    rgbTotal = [0, 0, 0]
    for pixel in data:
        for colorIndex in range(0, 3):
            rgbTotal[colorIndex] += pixel[colorIndex]
    
    return rgbTotal


if(len(argv) < 2):
    print("You should specify filepath")
    exit()

filePath = argv[1]

with Image.open(filePath) as image:
    colorsNames = ["Red", "Green", "Blue"]
    totalWeights = get_total_colors_weights(image)
    maxValueIndex = list.index(totalWeights, max(totalWeights))
    print(f"Most of the colors in the image are {colorsNames[maxValueIndex]}")