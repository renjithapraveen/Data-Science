import cv2

# 1. Load the pre-trained Haar Cascade XML model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 2. Read the target image and convert it to grayscale 
# (Haar cascades process pixel intensity differences, so color isn't needed)
img = cv2.imread('person.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Detect objects using the classifier configuration parameters
faces = face_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.1,  # Compels processing adjustments across scales
    minNeighbors=5,   # Filters out overlapping false positives
    minSize=(30, 30)  # Skips faces smaller than 30x30 pixels
)

# 4. Extract bounding box coordinates and paint them onto your image
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the outcome window
cv2.imshow('Object Detection Active', img)
cv2.waitKey(0)
cv2.destroyAllWindows()