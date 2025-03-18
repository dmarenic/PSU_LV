import numpy as np
import matplotlib.pyplot as plt

def chessboard(square_size, rows, cols):
    # Kreiranje osnovne crno-bijele pločice (2x2 kvadrata)
    tile = np.array([[0, 255], [255, 0]], dtype=np.uint8)

    # Ponavljanje pločice kako bismo dobili željeni broj redaka i stupaca
    board = np.tile(tile, (rows // 2, cols // 2))

    # Skaliranje na željenu veličinu piksela
    img = np.kron(board, np.ones((square_size, square_size), dtype=np.uint8))

    return img

# Parametri
square_size = 50  # Veličina kvadrata u pikselima
rows, cols = 4, 5  # Broj kvadrata u visini i širini

# Generiranje šahovskog polja
img = chessboard(square_size, rows, cols)

# Prikaz slike
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
