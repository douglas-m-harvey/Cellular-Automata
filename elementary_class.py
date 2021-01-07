import numpy as np
import matplotlib.pyplot as plt
import itertools


class CellularAutomaton:
    
    def __init__(self, gens, cols, rule):
        self.gens = gens
        self.cols = cols
        self.rule = rule
    
    
        # Define the initial row.
        self.grid = np.random.choice([0, 1], (1, cols))
        
        # grid[0][cols//2 + (cols % 2 > 0) - 1] = 1
        
        # List all 3-element combinations of 0 and 1.
        self.combinations = list(map(list, itertools.product([1, 0], repeat = 3)))
        
        # Convert rule to binary.
        self.ruleBinary = [int(char) for char in "{0:08b}".format(rule)]
        
        
        # Do all the actual maths, make rows and add them to the array.
        for gen in range(gens):
            row = np.zeros((1, cols))
            for cell in range(cols):
                # Construct an array from 3 neighbouring cells,wrapping back round
                # at the edges. Replacing -(cell - 1) with (1 + cell) is cool.
                smallArray = np.roll(self.grid[gen].copy(), -(cell - 1))[0:3]
                for i, state in enumerate(self.combinations):
                    if np.array_equal(smallArray, state):
                        row[0][cell] = self.ruleBinary[i]
            self.grid = np.append(self.grid, row, axis = 0)
        
    def displayGrid(self):
        fig = plt.figure(figsize = (12, 12))
        plt.title("gens: " + str(self.gens) + ", rules: " + str(self.rule))
        plt.imshow(self.grid)
        plt.show()
        
    def printRuleBinary(self):
        for i, combination in enumerate(self.combinations):
            print(combination, " - ", self.ruleBinary[i], "\n")
        
        # Find a way of identifying repeats
        # Expand cols to fit each generation
        # Define cells as dictionaries with value, colour, type, etc.