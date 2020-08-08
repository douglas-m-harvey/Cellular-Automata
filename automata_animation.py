# https://stackoverflow.com/questions/17212722/matplotlib-imshow-how-to-animate
# https://www.geeksforgeeks.org/conways-game-life-python-implementation/


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import product
import templates as tm


fps = 8
nSeconds = 16
    
x, y = 40, 40
B = [3]
S = [2, 3]

# startGrid = np.random.choice([0, 0, 1], (x, y))
startGrid = np.zeros((x, y))

tm.addGlider(6, 6, startGrid)
snapshots = [startGrid]  

# Define the rules and make the images! 
for n in range(nSeconds*fps - 1):
    image = snapshots[n].copy()
    newImage = np.zeros((x, y))
    for i, j in product(range(x), range(y)):
        if x - 1 > i > 0 and y - 1 > j > 0:
            smallArray = image.copy()[(i-1):(i+2), (j-1):(j+2)]
            smallArray[1][1] = 0
            neighbours = np.sum(smallArray)
            if image[i][j] == 0 and neighbours in B:
                newImage[i][j] = 1
            elif image[i][j] == 1 and neighbours in S:
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
# anim.save('test_anim.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])