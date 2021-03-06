'''
Control a DSLR camera for image capture and transfer.
'''

import logging
from time import sleep

import cv2

class Camera:

    def __init__(self):

        # Select the first available camera device
        self._cam = cv2.VideoCapture(0)

        # Make sure camera is opened
        if not self._cam.isOpened():
            raise IOError("Failed to access camera. Make sure it is connected and powered on.")

    def __del__(self):
        self._cam.release()

    def capture(self, savepath):
        '''Capture a single image and save it to savepath'''

        ret, frame = self._cam.read()

        # ret is True if the frame was correctly received, False otherwise
        if not ret:
            raise IOError("Cannot receive frame. Make sure camera is on and connected.")

        cv2.imwrite(savepath, frame)

def camera_full(savepath):

    res = False

    # Select the first available camera device
    cam = cv2.VideoCapture(0)

    try:
        # Make sure camera is opened
        if not cam.isOpened():
            raise IOError("Failed to access camera. Make sure it is connected and powered on.")

        ret, frame = cam.read()
        logging.debug("Camera - Finished read operation")

        sleep(0.1)

        # ret is True if the frame was correctly received, False otherwise
        if not ret:
            raise IOError("Cannot receive frame. Make sure camera is on and connected.")

        logging.debug("Camera - Writing image to disk")
        cv2.imwrite(savepath, frame)
        
        res = True

    finally:
        logging.debug("Camera - Releasing camera")
        cam.release()

    return res