from argparse import ArgumentParser
from moviepy.editor import VideoFileClip

parser = ArgumentParser()

parser.add_argument("--file", required=True, help="File to analyze")
parser.add_argument("--start", required=True, help="Starting position")
parser.add_argument("--end", required=True, help="Ending position")
parser.add_argument("--outputFile", default="result.mp4", help="Output file name, default: result.mp4")
args = parser.parse_args() 

with VideoFileClip(args.file) as videoFile:
    resultClip = videoFile.subclip(args.start, args.end)

    resultClip.write_videofile(args.outputFile)
