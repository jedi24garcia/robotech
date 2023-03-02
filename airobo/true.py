#!/usr/bin/env python3

""" We are learning NumPy """ 

import numpy
from scipy import misc 
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

A = imread('Tiger.jpg');
type(A)

numpy.ndarray

plt.imshow(A)
plt.show()
