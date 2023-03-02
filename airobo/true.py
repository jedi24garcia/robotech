#!/usr/bin/env python3

""" We are learning NumPy """ 

import numpy
from scipy import misc 
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread('Tiger.jpg');
type(img)

numpy.ndarray

plt.imshow(img)
plt.show()
