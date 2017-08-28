import cv2
import numpy as np

# Read and convert to gray image
left = cv2.imread('../images/right_2.jpg')
left = cv2.cvtColor(left, cv2.COLOR_RGB2GRAY)

# Read and convert to gray image
right = cv2.imread('../images/right.jpg')
right = cv2.cvtColor(right, cv2.COLOR_RGB2GRAY)

sub_matrix = left -right
cv2.imshow('The differences', sub_matrix)
cv2.waitKey()
cv2.destroyAllWindows()
