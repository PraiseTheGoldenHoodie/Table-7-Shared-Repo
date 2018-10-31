import numpy as np
import matplotlib.pyplot as plt

# Data
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 5.0)
y1 = np.cos(x1)
y2 = np.sin(x2)

# Creates 2 subplots w/ shared y axis and x axis
fig, (ax1, ax2) = plt.subplots(2,sharey=True)

ax1.plot(x1, y1)
ax1.set(title=' 2 subplots', ylabel='y1 value')

ax2.plot(x2, y2)
ax2.set(xlabel='x value', ylabel='y2 value')

plt.show()
