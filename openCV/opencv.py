import cv2
'''img = cv2.imread('image/images.jpeg', -1)
print(img)
# cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyWindow()'''


# For resizing the image
'''cv2.imshow("Picture", img)
resize = cv2.resize(img, (256, 256))
cv2.imshow("Picture", img)
cv2.imshow("Resized Picture", resize)# Resized Image
cv2.waitKey(0)'''

# For greyscale image:
'''gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey image", gray)
cv2.waitKey(5000)'''

# # For a Blur image
'''blur = cv2.GaussianBlur(gray, (19,19), 0)

cv2.imshow("Blur Picture", blur) # Display Blur image
cv2.waitKey(0)'''


# Draw a line
import numpy as np
'''

img = np.zeros((512,512,3))

img = cv2.line(img,(0,0),(511,511),(255,0,0),10)

cv2.imshow("Line", img) # Display the line cutting through the image
cv2.waitKey(0)'''

# To inserting the text:
'''img = np.zeros((512, 512, 3))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Computer Vision', (125, 250), font, 1, (0, 0, 255), 3, cv2.LINE_AA)
cv2.imshow("Text", img)
cv2.waitKey(0)'''

# Drawing polygons
'''img = np.zeros((512,512,3))

pts = np.array([[25, 70], [25, 160],
                [110, 200], [200, 160],
                [200, 70], [110, 20]],
               np.int32)

pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow("Polygon", img) # Display the Hexagon
cv2.waitKey(0)'''

# Video Capturing/ Access the webcam:
''''# cap = cv2.VideoCapture(0)
Video = cv2.VideoCapture('/home/ta2/Downloads/videoplayback.mp4')
while True:
    ret, frame = Video.read()
    cv2.imshow("Capture", frame)
    key = cv2.waitKey(3000)

    if (key == ord('q')):
        break
Video.release()
cv2.destroyWindow()'''
import matplotlib as plt
image = cv2.imread('/kaggle/input/opencv-samples-images/data/building.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(20, 20))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)


# Create our shapening kernel, we don't normalize since the
# the values in the matrix sum to 1
kernel_sharpening = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])

# applying different kernels to the input image
sharpened = cv2.filter2D(image, -1, kernel_sharpening)


plt.subplot(1, 2, 2)
plt.title("Image Sharpening")
plt.imshow(sharpened)

plt.show()