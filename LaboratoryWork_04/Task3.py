from argparse import ArgumentParser
import cv2
from time import time
from pathlib import Path

parser = ArgumentParser()

parser.add_argument("--file", required=True, help="File to play")
args = parser.parse_args() 

filePath = Path(args.file)

cap = cv2.VideoCapture(filePath)
frameTime = int(1000 / cap.get(cv2.CAP_PROP_FPS))

lastFrameTime = time() - (frameTime / 1000)
while cap.isOpened():
    success, frame = cap.read()
 
    currentFps = 1 / (time() - lastFrameTime)
    lastFrameTime = time()
    textToPut = f"FPS: {currentFps}" 
    cv2.putText(frame, textToPut, (0, 20), 1, 1, (255, 255, 255))
    cv2.putText(frame, filePath.name, (0, 40), 1, 1, (255, 255, 255))
    if not success:
        break

    cv2.imshow('frame', frame)
    cv2.waitKey(frameTime) # for some reason, its not working with the regular sleep

 
cap.release()
cv2.destroyAllWindows()