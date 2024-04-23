import pytesseract
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = "Call.jpg"
image = Image.open(image_path)
text = pytesseract.image_to_string(image)
print("TEXT FROM PICTURE:\n")
print(text)

img = cv2.imread("newTest.png")
plt.imshow(img[:,:,::-1])
plt.show()

sr = cv2.dnn_superres.DnnSuperResImpl_create()
 
path = "EDSR_x4.pb"
 
sr.readModel(path)
 
sr.setModel("edsr",4)
 
result = sr.upsample(img)
 
# Resized image
resized = cv2.resize(img,dsize=None,fx=4,fy=4)
 
plt.figure(figsize=(12,8))
plt.subplot(1,3,1)
# Original image
#plt.imshow(img[:,:,::-1])
plt.subplot(1,3,2)
# SR upscaled
#plt.imshow(result[:,:,::-1])
plt.subplot(1,3,3)
# OpenCV upscaled
plt.imshow(resized[:,:,::-1])
plt.show()
plt.savefig("EDSR.jpg")

# sr = cv2.dnn_superres.DnnSuperResImpl_create()
# path = "ESPCN_x4.pb"
# sr.readModel(path)
# sr.setModel("espcn", 4)
# result=sr.upsample(image_path)
