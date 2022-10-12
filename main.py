# import urllib.request as request
# import numpy as np
# import cv2
# from PIL import Image
# import time
# url = 'http://192.168.80.53:8080/shot.jpg'       # to send image as input, change it according to provided
# while True:
#     img = request.urlopen(url)      # It will give the object of the url
#     img_bytes = bytearray(img.read())   # To convert image to bytes
#     img_np = np.array(img_bytes, dtype=np.uint8)
#     frame = cv2.imdecode(img_np, -1)        # To decode the image,  -1 represent image is unchanged and if it is 0 then image is grey scale
#     frame_cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      # To change colour of image
#     frame_blur = cv2.GaussianBlur(frame_cvt, (5, 5), 0)     # For smoothing and bluring
#     frame_edge = cv2.Canny(frame_blur, 30, 50)      # Canny => To detect the edges
#     contours, h = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)      # To get the shape of object
#     if contours:
#         max_contour = max(contours, key=cv2.contourArea)    # To get the biggest contour in terms of area
#         x, y, w, h = cv2.boundingRect(max_contour)      # To get the x and y axis and width and height of biggest rect
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
#     cv2.imshow('My Smart Scanner', frame)         # To open a popup to show the image,   You can also use frame in place of object_only if image edges are large
#     if cv2.waitKey(1) == ord('s'):      # Press s key to save the image
#         img_pil = Image.fromarray(frame)
#         time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
#         img_pil.save(f'{time_str}.pdf')         # To save the image in same folder and in this order
#         print(time_str)





import urllib.request as request
import numpy as np
import cv2
from PIL import Image
import time
url = 'http://192.168.80.53:8080/shot.jpg'       # to send image as input, change it according to provided
while True:
    img = request.urlopen(url)      # It will give the object of the url
    img_bytes = bytearray(img.read())   # To convert image to bytes
    img_np = np.array(img_bytes, dtype=np.uint8)
    frame = cv2.imdecode(img_np, -1)        # To decode the image,  -1 represent image is unchanged and if it is 0 then image is grey scale
    frame_cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      # To change colour of image
    frame_blur = cv2.GaussianBlur(frame_cvt, (5, 5), 0)     # For smoothing and bluring
    frame_edge = cv2.Canny(frame_blur, 30, 50)      # Canny => To detect the edges
    contours, h = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)      # To get the shape of object
    if contours:
        max_contour = max(contours, key=cv2.contourArea)    # To get the biggest contour in terms of area
        x, y, w, h = cv2.boundingRect(max_contour)      # To get the x and y axis and width and height of biggest rect
        if cv2.contourArea(max_contour) > 5000:
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            object_only = frame[y:y+h, x:x+w]   # frame[vertical, horizantal]
            cv2.imshow('My Smart Scanner', object_only)         # To open a popup to show the image,   You can also use frame in place of object_only if image edges are large
            if cv2.waitKey(1) == ord('s'):      # Press s key to save the image
                img_pil = Image.fromarray(object_only)
                time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
                img_pil.save(f'{time_str}.pdf')         # To save the image in same folder and in this order
                print(time_str)