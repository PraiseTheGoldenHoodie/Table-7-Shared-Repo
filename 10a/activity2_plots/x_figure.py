import matplotlib.pyplot as plt
import matplotlib.lines as lines

# Will draw an X


thing = plt.figure()                # Thing is a figure

line1 = lines.Line2D([0, 1], [0, 1], transform = thing.transFigure, figure = thing)

line2 = lines.Line2D([0, 1], [1, 0], transform = thing.transFigure, figure = thing)

thing.lines.extend([line1, line2])

plt.show()