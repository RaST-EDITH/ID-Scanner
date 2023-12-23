import numpy as np
import cv2
from pyzbar.pyzbar import decode
# import pytesseract

def checkFace( img ) :
    # To detect the face in the image

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(r"C:\Users\ASUS\OneDrive\Documents\GitHub\ID-Scanner\haarcascade_frontalface_default.xml")
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

        # Define the corner coordinates
        corner1 = ptr.polygon[0]
        corner2 = ptr.polygon[1]
        corner3 = ptr.polygon[2]
        corner4 = ptr.polygon[3]

        # Create an array of the corner coordinates
        pts = np.array([corner1, corner2, corner3, corner4], np.int32)
        pts = pts.reshape((-1, 1, 2))

        # Draw the quadrilateral on the image
        cv2.polylines(img, [pts], True, (0, 255, 0), 2)

        # cv2.rectangle(img, ptr.polygon[0], ptr.polygon[1], ptr.polygon[2], ptr.polygon[3], ( 0, 255, 0), 2)

        cv2.imshow('Detected QR', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def locateId( img ) :
    # To locate the id in the frame

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original', img)
    edges = cv2.Canny( gray_img, 50, 100)
  
    # Display edges in a frame
    cv2.imshow('Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread(r"image")
# locateId( img )
checkFace( img )
checkBarcode( img )
