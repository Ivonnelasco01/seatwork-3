#import
import urllib.request as request
import numpy as np
import cv2
from PIL import Image
#paste ip in variable
url = 'http://192.168.0.102:8080/shot.jpg'

while True:
    #open img
    img = request.urlopen(url)
    #convert img to bytes
    img_bytes = bytearray(img.read())
    img_np = np.array(img_bytes, dtype=np.uint8)
    frame = cv2.imdecode(img_np, -1)
    frame_cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_blur = cv2.GaussianBlur(frame_cvt, (5, 5), 0)
    frame_edge = cv2.Canny(frame_blur, 30, 50)
    #show the img
    cv2.imshow('Smart Scanner', frame_edge)
    contours, h = cv2.findCountors(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
    #save img
    if cv2.waitKey(1) == ord('s'):
        img_pil = Image.fromarray(frame)
        time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
        img_pil.save(f'{time_str}.pdf')
        print(time_str)
