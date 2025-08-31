import os  #it is a python built in module to interact with operating systems


import cv2  #opencv library for python

#read path:
image_path=os.path.join('..','data','image1.webp')
print("Looking for:", image_path)  # debug
img=cv2.imread(image_path)

if img is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

#write image:
cv2.imwrite(os.path.join('..','data','image2.webp'),img)


#visualize image:
cv2.imshow('image',img)
cv2.waitKey(0)   #waitkey means for how much time image will be displayed , 0 means until we close it.
