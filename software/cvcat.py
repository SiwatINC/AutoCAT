import cv2
from PIL import ImageGrab, Image
import numpy as np
def detectCat(image: Image):
    image = np.asarray(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier('software/haarcascade_frontalcatface_extended.xml')
    rects = detector.detectMultiScale(gray, scaleFactor=1.3,minNeighbors=10, minSize=(75, 75))
    return rects