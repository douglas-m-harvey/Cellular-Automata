import numpy as np
import matplotlib.pyplot as plt
import itertools
import random as rn


# Define grid size parameters.
gens = 100
cols = 2*gens + 1

# Define rules and the generations from which each is applied
genList = [0, 20, 40, 60, 80]
ruleList = [rn.randint(1, 255) for _ in range(5)]

# Define the initial row.
grid = np.random.choice([0, 1], (1, cols))
# Add specific True cells in initial row. // is integer division,
# (cols % 2 > 0) rounds up to the nearest integer.
# grid[0][cols//2 + (cols % 2 > 0) - 1] = 1

# List all 3-element combinations of 0 and 1.
combinations = list(map(list, itertools.product([1, 0], repeat = 3)))


# Do all the actual maths, make rows and add them to the array.
for gen in range(gens):
    row = np.zeros((1, cols))
    # Define a rule from ruleList depending on generation.
    if gen in genList:
        rule = ruleList[genList.index(gen)]
        # Convert rule to binary.
        ruleBinary = [int(char) for char in "{0:08b}".format(rule)]
    for cell in range(cols):
            # Construct an array from 3 neighbouring cells,wrapping back round
            # at the edges. Replacing -(cell - 1) with (1 + cell) is cool.
            smallArray = np.roll(grid[gen].copy(), -(cell - 1))[0:3]
            for i, state in enumerate(combinations):
                if np.array_equal(smallArray, state):
                    row[0][cell] = ruleBinary[i]
    grid = np.append(grid, row, axis = 0)


fig = plt.figure(figsize = (12, 12))
plt.title("genList: " + str(genList) + ", ruleList: " + str(ruleList))
plt.imshow(grid)
plt.show()

for i, combination in enumerate(combinations):
    print(combination, " - ", ruleBinary[i], "\n")

# Find a way of identifying repeats
# Expand cols to fit each generation
# Define cells as dictionaries with value, colour, type, etc.