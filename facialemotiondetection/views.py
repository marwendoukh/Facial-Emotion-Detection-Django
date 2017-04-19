from django.http import HttpResponse
import cv2
from django.shortcuts import render


def index(request):
  while (True):

    cascPath = "/home/marwen/Downloads/djangoTesting/Django_face_recognition/website/mysite/opencv/haarcascade_frontalface_default.xml"
    i = 0
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)

    # Capture frame-by-frame
    ret, frame = video_capture.read()


    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(2, 2),
       # flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    # print faces found ......
    facesNumber ="Found {0} faces!".format(len(faces))

    return render(request, 'result.html', {'p': facesNumber})
