import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.arange(0.0, 2.0, 0.01)
y = 5 * np.pi * x
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel='x value', ylabel='y value',
       title='simple plot')
ax.grid()
fig.savefig("test.png")
plt.show()
