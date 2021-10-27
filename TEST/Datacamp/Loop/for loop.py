#for var in seq:
#    expression

fam = [1.73, 1.68, 1.71, 1.89]

for height in fam:
    print(height)

for index,height in enumerate(fam):
    print("Index: "+ str(index) + ": " + str(height))

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for i in areas:
    print(i)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for x,y in enumerate(areas):
    print("room "+ str(x) + ": " + str(y))

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+ 1) + ": " + str(area))

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch = the x is y sqm
for x,y in list(house):
    print("the " +str(x)+ " is " + str(y) + " sqm")