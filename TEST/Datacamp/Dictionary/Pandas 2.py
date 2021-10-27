import pandas as pd

brics = pd.read_csv("/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/brics.csv", index_col=0)



# Import cars data
import pandas as pd
cars = pd.read_csv('/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars[["country", "drives_right"]])


# Import cars data
import pandas as pd
cars = pd.read_csv('/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])


# Import cars data
import pandas as pd
cars = pd.read_csv('/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc["JAP"])
print(cars.iloc[2])
# Print out observations for Australia and Egypt
print(cars.loc[["AUS",'EG']])
print(cars.iloc[[1,-1]])




# Print out drives_right value of Morocco
print(cars.loc[['MOR'],["drives_right"]])

# Print sub-DataFrame
print(cars.loc[['MOR',"RU"],["drives_right",'country']])


# Print out drives_right column as Series
print(cars.loc[:,"drives_right"])

# Print out drives_right column as DataFrame
print(cars.loc[:,["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,["cars_per_cap","drives_right"]])
