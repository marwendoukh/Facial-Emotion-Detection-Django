from django.http import HttpResponse
import cv2


def index(request):
  while (True):

    imagePath = "/home/marwen/Downloads/djangoTesting/Django_face_recognition/website/mysite/opencv/passenger2.jpg"
    cascPath = "/home/marwen/Downloads/djangoTesting/Django_face_recognition/website/mysite/opencv/haarcascade_frontalface_default.xml"
    i = 0
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Read the image
    image = cv2.imread(imagePath,1)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(2, 2),
       # flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    facesNumber ="Found {0} faces!".format(len(faces))
    cv2.imwrite("/home/marwen/Downloads/djangoTesting/Django_face_recognition/website/mysite/opencv/passenger_facesDDDDDD.jpg", frame)

    return HttpResponse(facesNumber)
