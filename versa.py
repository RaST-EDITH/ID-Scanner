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

    for (x, y, w, h) in face_rtg:
        cv2.rectangle(img, (x-10, y-25), (x+w+6, y+h+20), ( 0, 255, 0), 2)

    imgRoi = img[y:y+h,x:x+w]

    cv2.imshow('Detected face', img)
    # cv2.imshow('Face', imgRoi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def checkBarcode( img ) :
    # To detect the barcode in the image
    # print(decode(img))

    for ptr in decode(img) :
        print( ptr.data.decode())

        # print( ptr.rect)
        # x, y, w , h = ptr.rect
        # print(x,y,w,h)

        # print( ptr.polygon)
