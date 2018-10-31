import numpy as np
import matplotlib.pyplot as plt


radius = np.arange(0, 5, 0.15)
theta = 2 * np.pi * radius

ax = plt.subplot(111, projection = 'polar')
ax.plot(theta, radius)
ax.set_rmax(5)
ax.set_rticks([1 , 2 , 3 , 4 , 5])
ax.set_rlabel_position(-30)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plotted on a polar axis", va = 'bottom')
plt.show()