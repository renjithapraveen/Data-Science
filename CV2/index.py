import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), dtype=np.uint8)

# Unfilled red circle
cv2.circle(img, (100, 100), 50, (0, 0, 255), 5)

# Filled blue square
cv2.rectangle(img, (180, 200), (280, 300), (255, 0, 0), -1)

# Unfilled green square
cv2.rectangle(img, (350, 20), (480, 150), (0, 255, 0), 5)

# Filled red circle
cv2.circle(img, (380, 400), 50, (0, 0, 255), -1)

# White diagonal line
cv2.line(img, (0, 0), (500, 500), (255, 255, 255), 5)

# Display image
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()