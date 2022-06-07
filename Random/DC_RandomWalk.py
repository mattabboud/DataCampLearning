# NumPy is imported, seed is set
import numpy as np

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Set the seed
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine next step
    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
        print("You rolled a :" + str(dice))
    elif dice <= 5:
        step = step + 1
        print("You rolled a :" + str(dice))
    else:
        print("You rolled a :" + str(dice) + " !!!")
        addRoll = np.random.randint(1, 7)
        print("You rerolled a : " + str(addRoll))
        step = step + addRoll

    # append next_step to random_walk
    random_walk.append(step)
    print("You are on Step : " + str(step))

# Print random_walk
print(random_walk)
print(len(random_walk))

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
