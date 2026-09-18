import cv2
import numpy as np

# Read image
img = cv2.imread("shapes.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    # Ignore tiny contours
    area = cv2.contourArea(cnt)
    if area < 100:
        continue

    # Ignore image border
    if area > 100000:
        continue

    # Function able to identify the points defining our shape
    approx = cv2.approxPolyDP(cnt,0.01 * cv2.arcLength(cnt, True),True)

    n = len(approx)

    if n == 6:
        # Hexagon
        print("We have a hexagon here")
        cv2.drawContours(img, [cnt], 0, (255, 0, 255), 3)

    elif n == 3:
        # Triangle
        print("We found a triangle")
        cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

    elif n > 9:
        # Circle
        print("We found a circle")
        cv2.drawContours(img, [cnt], 0, (0, 255, 255), 3)

    elif n == 4:
        # Square
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h

        if 0.95 <= aspect_ratio <= 1.05:
            print("We found a square")
            cv2.drawContours(img, [cnt], 0, (255, 255, 0), 3)
        else:
            print("We found a rectangle")
            cv2.drawContours(img, [cnt], 0, (255, 0, 0), 3)

# Show result
cv2.imshow("Detected Shapes", img)

cv2.waitKey(0)
cv2.destroyAllWindows()