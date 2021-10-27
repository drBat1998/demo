import numpy as np
import pandas as pd
brics = pd.read_csv("/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/brics.csv", index_col=0)

is_huge = brics["area"]>8

print(brics[is_huge])

# or
print(brics[brics["area"]>8])

# less than 10

print(brics[np.logical_and(brics["area"]>8,brics["area"]<10)])

# Import cars data
import pandas as pd
cars = pd.read_csv('/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr]==True

# Print sel
print(sel)

# Convert code to a one-liner
sel = cars[cars['drives_right']==True]

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]

many_cars =cpc >500
car_maniac = cars[many_cars]
# Print car_maniac
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)