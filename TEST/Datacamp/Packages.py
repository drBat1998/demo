# Install packages
# http://pip.readthedocs.org/en/stable/installing/
# https://pip.pypa.io/en/stable/installation/
# Download get-pip.py
# Terminal: python3 get-pip.py then pip3 install numpy
#$ python get-pip.py

#get-pip.py
# Import package - The best varient
import numpy
numpy.array([1,2,3])

# Next way
import numpy as np
np.array([1,2,3])

# Therd way - not so good
from numpy import array
array([1,2,3])

# Imoort package
## Definition of radius
r = 0.43
## Import the math packafe
import math

## C = 2πr
C = 2* math.pi*r

## A = πr^2
A = math.pi *r**2

## Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


# Selective import
from math import pi
## Definition of radius
r = 192500

## Import radians function of math package
from math import radians

## Travel distance of Moon over 12 degrees. Store in dist.
dist = radians(r)* 12

## Print out dist
print(dist)