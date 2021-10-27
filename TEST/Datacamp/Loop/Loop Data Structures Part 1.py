#for var in seq:
#      expression
world = {
    "afghanistan":30.55,
    "albania": 2.77,
    "algeria": 39.21
}
for k,v in world.items():
    print(k+ " -- " + str(v))

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height,np_weight])

for val in np.nditer(meas):
    print(val)


europe = {
    "spain":"madrid",
    "france": "paris",
    "germany": "berlin",
    "norway": "oslo",
    "italy": "rome",
    "poland": "warsaw",
    "austria": "vienna"
}

# Iterate over europe
for x,y in europe.items():
    print("the capital of "+ x + " is " + y)

np_baseball = np.array([[1,2,3,4,5,6,7,8,9,10],[21,22,34,45,67,89,90,95,100,120]])
# Import numpy as np
import numpy as np

# For loop over np_height
for x,y in np.nditer(np_height):
    print(str(x) + " inches")


# For loop over np_baseball
for var in np.nditer(np_baseball):
    print(np_baseball)