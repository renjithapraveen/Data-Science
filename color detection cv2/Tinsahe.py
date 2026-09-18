import cv2
import numpy as np

# Read image
img = cv2.imread("shapes.png")

# Check if image loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert BGR to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Blue color range
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

# Create mask
mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

# Extract blue object
result = cv2.bitwise_and(img, img, mask=mask)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("HSV Image", hsv_img)
cv2.imshow("Blue Mask", mask)
cv2.imshow("Blue Detection", result)

cv2.waitKey(0)
cv2.destroyAllWindows()