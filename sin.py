import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 2 * np.pi, 0.001)
y = np.sin(t)

plt.plot(t, y)
plt.show()
