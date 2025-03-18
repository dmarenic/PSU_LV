import numpy as np
import matplotlib.pyplot as plt

# Definiranje koordinata točaka
x = np.array([1, 2, 3, 3, 1])
y = np.array([1, 2, 2, 1, 1])

# Crtanje grafa
plt.plot(x, y, marker='o', color='red', linestyle='-', linewidth=4, markersize=10)

# Dodavanje oznaka
plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Primjer")

# Postavljanje granica osi
plt.xlim(0, 4)
plt.ylim(0, 4)

# Prikaz slike
plt.grid(True)
plt.show()
