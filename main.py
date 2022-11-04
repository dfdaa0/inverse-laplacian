from lib import *
import matplotlib.pyplot as plt
import numpy as np
import cv2

img = plt.imread("") # Write the image path between quotation marks (use a B&W image)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # The image needs to be grayscaled

kernel = np.array([[0,1,0],
                   [1,-4,1],
                   [0,1,0]])/6 # Change the values and see different behaviours

rows, columns = img.shape
psf = np.zeros((rows,columns)) # A full size representation of the Kernel
psf[0:rows,0:columns] = kernel

kernelFourier = dft(psf)
kernelFourier = switches0by1(kernelFourier) # Sometimes it is necessary

originalFunction = idft(dft(img) / dft(psf))
plt.imshow(originalFunction.real)
plt.show()