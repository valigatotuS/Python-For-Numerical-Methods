
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3] 
y = [0, 1, 4, 9]
plt.plot(x, y)
plt.show()

x = np.linspace(-5,5, 10)
plt.plot(x, x**2, 'g--')
plt.show()