import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 10, 20, 30, 40])
ypoints = np.array([0, 250, 1500, -1000, -800])

plt.plot(xpoints, ypoints)
plt.show()

# just points
plt.plot(xpoints, ypoints, 'o')
plt.show()

# Plotting without x-points:
plt.plot(ypoints)
plt.show()

# just points and plotting without x-points:
plt.plot(ypoints, 'o')
plt.show()