import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi*4, np.pi*4, 256, True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)
plt.show()
