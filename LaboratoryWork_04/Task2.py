from argparse import ArgumentParser
from moviepy.editor import VideoFileClip
from skimage import io, transform
from numpy import uint8
from pathlib import Path

parser = ArgumentParser()

parser.add_argument("--file", required=True, help="File to analyze")
parser.add_argument("--start", required=True, type=int, help="Starting position")
parser.add_argument("--end", required=True, type=int, help="Ending position")
parser.add_argument("--timeStep", default=10, type=int, help="Time step between frames, default: 10")
parser.add_argument("--outputFolder", default="result", help="Output folder name, default: result")
args = parser.parse_args() 

with VideoFileClip(args.file) as videoFile:
    print(videoFile.size)
    resizeFactor = min(1, 250 / videoFile.size[1])
    newSize = (videoFile.size[0] * resizeFactor, videoFile.size[1] * resizeFactor)

    outputFolder = Path(args.outputFolder)
    outputFolder.mkdir(exist_ok=True)
    for index, timeStamp in enumerate(range(args.start, args.end, args.timeStep)):
        currentFrame = videoFile.get_frame(timeStamp)
        imageToSave = (transform.resize(currentFrame, reversed(newSize))*255).astype(uint8)
        io.imsave(outputFolder.joinpath(f"{index:02}.jpg"), imageToSave)