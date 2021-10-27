# 10.08.21 I try to test python's lists

# lists
test1 = [1, 2, 3, 4, 5]
test2 = ["lol", "try be easy", "to do"]
test3 = [test1, test2]

print(test3)

test4 = test1[:2]
print(test4)

# if statement
x = 5
if x > 4:
    print("lol")
else:
    print("fuck")
print(test1)

y = 100
if y > 100:
    print(test1)
elif y == 100:
    print(test2)
else:
    print(test3)

# Methods
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.index("mom") # "Call methof"
fam.count(1.73)
sister = "liz"
sister.capitalize()
sister.replace("l","Be" )

fam.append(2.32)
