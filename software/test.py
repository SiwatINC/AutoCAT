import cvcat
from PIL import ImageGrab
image = ImageGrab.grab()
rect = cvcat.detect_cat(image)
if len(rect) >0:
    print("found cat at " + str(rect))
else:
    print("not a cat")