import numpy as np
import cv2
from pyzbar.pyzbar import decode
# import pytesseract

def checkFace( img ) :
    # To detect the face in the image

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(r"C:\Users\ASUS\haarcascade_frontalface_default.xml")
    face_rtg = faceCascade.detectMultiScale(gray_img, 1.3, 9)
    # print( face_rtg )
