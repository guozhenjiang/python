# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()            # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) # Plot some data on the axes.

plt.show()