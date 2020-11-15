import numpy
import cv2
img = cv2.imread("smallgray.png", 0)   # 0 is greyscale, # use 1 for bgr(numpy array)
# # print(img)
# # cv2.imwrite("newsmallgray.png", img)  # making images from numpy arrays
# print(img[0:2,2:4])

# for i in img.flat:          # prints the elements one by one
#     print(i)

# Stacking and splitting numpy arrays

# ims = numpy.hstack(img, img)   # this will show error since it takes only one argument
ims = numpy.hstack((img, img, img))      # using the argument as a tuple is the solution
# print(ims)

imsv = numpy.vstack((img, img, img))
# print(imsv)

lst = numpy.hsplit(imsv, 1)
print(lst)

lst = numpy.vsplit(imsv, 3)
print(lst)