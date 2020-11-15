import cv2
img = cv2.imread("smallgray.png", 0)   # 0 is greyscale, # use 1 for bgr(numpy array)
# print(img)
# cv2.imwrite("newsmallgray.png", img)  # making images from numpy arrays
print(img[0:2,2:4])

for i in img.flat:          # prints the elements one by one
    print(i)