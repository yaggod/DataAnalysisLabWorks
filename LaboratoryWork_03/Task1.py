from pathlib import Path
from argparse import ArgumentParser
from skimage import io, transform
from numpy import uint8, flipud

def rotate_clockwise(image):
    return transform.rotate(image, -90, True, preserve_range=True)

def rotate_counterclockwise(image):
    return transform.rotate(image, 90, True, preserve_range=True)

def mirror(image):
    return flipud(image)

def scale_05(image):
    return transform.resize(image, (image.shape[0] // 2, image.shape[1] // 2), preserve_range=True)

def swirl(image):
    return transform.swirl(image, preserve_range=True)

def complex_transform(image):
    return mirror(scale_05(swirl(image)))


allTheActions = {
    "rotateClockwise" :  rotate_clockwise,
    "rotateCounterclockwise" :  rotate_counterclockwise,
    "mirror" : mirror, 
    "scale05" : scale_05,
    "swirl" : swirl,
    "complexTransform" : complex_transform
}



parser = ArgumentParser()
parser.add_argument("--directory", default="LaboratoryWork_03\\img", help="Working directory path (default: current folder)")
for actionName in allTheActions.keys():
    parser.add_argument(f"--{actionName}", dest="actionsList", action="append_const", const=allTheActions[actionName])
args = parser.parse_args()
actionsToApply = args.actionsList or allTheActions.values()


workingDirectory = Path(args.directory)
filesPattern = workingDirectory.joinpath("*.jpg")
images = io.imread_collection(str(filesPattern))


newImages = []

for i in range(min(len(images), 20)):
    image = images[i]
    for action in actionsToApply:
        newImage = action(image).astype(uint8)
        newImages.append(newImage)



for i in range(len(newImages)):
    io.imsave(workingDirectory.joinpath(f"{i+min(len(images), 20):04}.jpg"), newImages[i])