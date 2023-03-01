import cv2

# Load the SVM model
svm = cv2.ml.SVM_load('svm.xml')

# Load the test image
img = cv2.imread('image/images.jpeg')

# Extract features from the test image
# You can use any feature detection algorithm here
# This example uses the HOG descriptor
hog = cv2.HOGDescriptor()
features = hog.compute(img)

# Reshape the feature vector to match the SVM model
features = features.reshape(1, -1)

# Predict whether the object is a car or not
result = svm.predict(features)

if result[1][0] == 1.0:
    print("Car detected!")
else:
    print("Not a car.")
