import numpy as np
print(np.random.seed(123))

coin = np.random.randint(0,2)

print(coin)
if coin == 0:
    print("heads")
else:
    print("tails")

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

# Numpy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)
# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice >=3 and dice <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

