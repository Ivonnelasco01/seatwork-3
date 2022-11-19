#import
import urllib.request as request
import numpy as np
import cv2
#paste ip in variable
url = "http://192.168.0.102:8080/shot.jpg"

while True:
    #open img
    img = request.urlopen(url)
    #convert img to bytes
    img_bytes = bytearray(img.read())
    img_np = np.array(img_bytes, dtype= np.uint8)
    frame = cv2.imdecode(img_np,0)
