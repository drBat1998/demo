import pandas as pd
brics = pd.read_csv("/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/brics.csv", index_col=0)

for lab,row in brics.iterrows():
    # - Creating series on every iteration
    brics.loc[lab,"name_length"] = len(row["country"])
print(brics)

# apply
brics["name_lenght"] = brics["country"].apply(len)
print(brics)

cars= pd.read_csv("/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/cars.csv", index_col=0)

for lab,row in cars.iterrows():
    print(lab)
    print(row)

for lab, row in cars.iterrows():
    print(lab + " : " + str(row["cars_per_cap"]))


# Import cars data
import pandas as pd
cars= pd.read_csv("/Users/romankoval/PycharmProjects/Learning/Datacamp/Dictionary/cars.csv", index_col=0)

# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)