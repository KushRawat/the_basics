import cv2
img = cv2.imread("smallgray.png", 1)   # 0 is greyscale, # use 1 for bgr(numpy array)
print(img)
cv2.imwrite("newsmallgray.png", img)  # making images from numpy arrays