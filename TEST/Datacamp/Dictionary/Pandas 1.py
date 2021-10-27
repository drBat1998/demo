# Pandas
import pandas as pd

dict = {
    "country": ["Brazil","Russia","India", "China", "South Africa" ],
    "capital": ["Brazilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area":[8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

brics = pd.DataFrame(dict)
print(brics)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

brics_1 = pd.read_csv("/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/brics.csv", index_col=0)
print(brics_1)


# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country":names,
           'drives_right': dr,
           'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)


import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("cars.csv")

# Print out cars
print(cars)


# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)