#!/usr/bin/env python3

""" We are learning NumPy """ 

import numpy
from scipy import misc 
import matplotlib.pyplot as plt

img = misc.face()
type(img)

numpy.ndarray

plt.imshow(img)
plt.show()
