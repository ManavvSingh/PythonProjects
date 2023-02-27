import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Chosse an image to detect faces in
img = cv2.imread('resources/images/jesse.webp')


# Must convert the image to gray scale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces 
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the face
for (x,y,w,h) in face_coordinates:
# (x,y,w,h) = face_coordinates[0] Haed code
    cv2.rectangle(img, (x,y), (x+w,y+h), (randrange(225),randrange(225),randrange(225)), 2)

# Display the image
cv2.imshow('face detector', img)

# Waits until a key is pressed
cv2.waitKey()

print('code completed')







'''
import cv2

# Loads pre trained frontal data from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Classifier - detector. 
# Detects the cascade xml file 

# Chosse an image to detect faces in
img = cv2.imread('images/jesse.webp')
# Use image read function from opencv

# Must convert the image to gray scale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# need to convert image to gray scale so there's just one type of color instead of RGB
# Using Convert color function 
# first arguement - image variable/Source image
# second argument - type of conversion 
# In opencv the color code is backwards ie instead of RGB it's BGR therefore BGR2GRAY

# Detect faces 
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# face_coordinates is a list within a list
# detectMultiScale - Detects objects of different sizes in the input image. Returns the coordinates of the image
# Detects the faces from the Classifier 'trained_face_data' no matter the Scale/size big or small
# Helps to draw the green rectangle around the detected face coordinates

# print(face_coordinates)

# Draw rectangles around the face
for (x,y,w,h) in face_coordinates:
# (x,y,w,h) = face_coordinates[0] Haed code
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,225,0), 5)
# Assigning the values of coordinates as x y w h
# face_coordinates[0] because face coordinates gives [[301,92,247,247]] so it is a list within a list and [301,92,247,247] is the 0th element of the list

# Hardcode:
# cv2.rectangle(img, (301,92), (247+301,247+92), (0,225,0), 2)

# # rectangle function is used to draw the rectangele shape
# First argument - top left and bottom right face_coordinates
# second argument - offset or (top+width, bottom+height)
# third argument - BGR color code 
# fourth argument - thickness of the line

# Display the image
cv2.imshow('face detector', img)
# Use image show function
# first value is name of the window that pops up and second value is the image variable

# Waits until a key is pressed
cv2.waitKey()
# Keeps the image open until a key is pressed and then proceeds with the execution

print('code completed')
'''