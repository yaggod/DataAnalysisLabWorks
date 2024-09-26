from skimage import transform
from numpy import flipud

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

