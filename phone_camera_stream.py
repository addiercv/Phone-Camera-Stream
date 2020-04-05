import urllib.request
import cv2
import numpy as np
import os
import time
from datetime import datetime

def main():
    # Check video download directory, grab frame size and create video write
    if saveVideo:
        if not os.path.isdir('downloads'):
            os.mkdir('downloads')
        name = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        filename = os.path.join('downloads', str(name) + '.avi')
        openURL = urllib.request.urlopen(URL)
        frame = np.array(bytearray(openURL.read()), dtype=np.uint8)
        frame = cv2.imdecode(frame, -1)
        frame_width, frame_height = frame.shape[0:2]
        vWriter = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), frameRate, (frame_height, frame_width))
    # Read frame, display and save video
    while True:
        # Use urllib to get the video frame
        openURL = urllib.request.urlopen(URL)
        # Read frame from URL in Numpy array
        frame = np.array(bytearray(openURL.read()), dtype=np.uint8)
        # Read image frame from a buffer in memory
        frame = cv2.imdecode(frame, -1)
        # Show image to target window
        if saveVideo: vWriter.write(frame)
        cv2.imshow('Camera Stream',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vWriter.release()

if __name__ == '__main__':
    URL = 'http://192.168.0.10:8080/shot.jpg'
    saveVideo = True
    frameRate = 30
    main()