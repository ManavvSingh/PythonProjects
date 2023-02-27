import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Chosse an image to detect faces in
# webcam = cv2.VideoCapture('resources/videos/gus.mp4')
webcam = cv2.VideoCapture(0)
# Runs the loop until successfull_frame_read is True
while True:

    # Read the current frames
    successfull_frame_read, frame = webcam.read()

    # Must convert the video to gray scale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces 
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the face
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (randrange(225),randrange(225),randrange(225)), 2)
    
    # Display the image
    cv2.imshow('face detector', frame)

    # Waits 1 millisecond for a key to be pressed and then itereates through while loop
    key = cv2.waitKey(1)

    if key == 81 or key==113:
        break

webcam.release()
print("Code completed")





'''
#import cv2
#from random import randrange

#trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Chosse an image to detect faces in
#webcam = cv2.VideoCapture('images/gus.mp4')

Runs the loop until successfull_frame_read is True
#while True:

    Read the current frames
    #successfull_frame_read, frame = webcam.read()
    successfull_frame_read is True when the read function works and there is value in frame
    frame is each second of data/video captured by webcam 
    
    Must convert the video to gray scale
    #grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Each value of frame or each frame is converted into a gray scaled image

    Detect faces 
    #face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    Draw rectangles around the face
    #for (x,y,w,h) in face_coordinates:
        # cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    Draws a rectangle on each frame of video
    
    Display the image
    #cv2.imshow('face detector', frame)
    Displays each frame

    Waits 1 millisecond for a key to be pressed and then itereates through while loop
    #key = cv2.waitKey(1)

    #if key == 81 or key==113:
        #break

# webcam.release()
# print("Code completed")
'''