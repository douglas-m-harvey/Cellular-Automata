# https://www.conwaylife.com/wiki/List_of_Life-like_cellular_automata
# http://www.mirekw.com/ca/rullex_life.html


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import product
import templates as tm


fps = 24
nSeconds = 8
save = False

# Rule in survival/birth format.
rule = "23/3"
# Convert the rulestring into a pair of lists.
survival = [int(char) for char in rule.split("/")[0]]
birth = [int(char) for char in rule.split("/")[1]]

# Define the starting grid size and any initial shapes.
size = (80, 80)
startGrid = np.random.choice([0, 0, 1], size)


# Define the rules and make the images! 
snapshots = [startGrid]
for n in range(nSeconds*fps - 1):
    image = snapshots[n].copy()
    newImage = np.zeros(size)
    for i, j in product(range(size[0]), range(size[1])):
        if size[0] - 1 > i > 0 and size[1] - 1 > j > 0:
            smallArray = image.copy()[i - 1:i + 2, j - 1:j + 2]
            smallArray[1][1] = 0
            neighbours = np.sum(smallArray)
            if image[i][j] == 0 and neighbours in birth:
                newImage[i][j] = 1
            elif image[i][j] == 1 and neighbours in survival:
                newImage[i][j] = 1
            else:
                newImage[i][j] = 0
        neighbours = 0
    snapshots.append(newImage)


# This bit animates, not sure how - check animation_example.py
fig = plt.figure(figsize=(10, 10))            
a = snapshots[0]
im = plt.imshow(a, interpolation = 'none', aspect = 'auto', vmin = 0, vmax = 1)
def animate_func(i):
    im.set_array(snapshots[i])
    return [im]
anim = FuncAnimation(fig, animate_func, frames = nSeconds*fps, interval = 1000/fps)
if save is True:
    anim.save('test_anim.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])