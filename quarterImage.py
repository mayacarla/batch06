#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program takes an image and returns the left corner

import matplotlib.pyplot as plt
import numpy as np

inF = input("Enter image file name: ")
outF = input("Enter output file: ")

img = plt.imread(inF)

height = img.shape[0]
width = img.shape[1]

img2 = img[height // 2:, :width//2]


plt.imshow(img2)
plt.show()
plt.imsave(outF, img2)

