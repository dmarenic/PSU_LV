import numpy as np
import matplotlib.pyplot as plt

# Učitavanje podataka iz mtcars.csv (uz pretpostavku da se datoteka nalazi u direktoriju PSU_LV/LV2/)
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

# Dodjela varijablama
mpg = data[:, 0]  # milje po galonu (potrošnja)
cyl = data[:, 1]  # broj cilindara
hp = data[:, 2]   # konjske snage
wt = data[:, 3]   # težina vozila

# b) Scatter plot: potrošnja (mpg) u odnosu na konjske snage (hp)
plt.figure(figsize=(8,6))
plt.scatter(hp, mpg, s=wt*50, c='blue', alpha=0.5, edgecolors="black")  # Veličina točke ovisi o težini

# Postavljanje oznaka i naslova
plt.xlabel("Konjske snage (hp)")
plt.ylabel("Potrošnja (mpg)")
plt.title("Ovisnost potrošnje o konjskim snagama")

# Prikaz grafa
plt.grid(True)
plt.show()

# d) Izračun minimalne, maksimalne i srednje vrijednosti potrošnje (mpg)
mpg_min = np.min(mpg)
mpg_max = np.max(mpg)
mpg_mean = np.mean(mpg)

print(f"Minimalna potrošnja: {mpg_min} mpg")
print(f"Maksimalna potrošnja: {mpg_max} mpg")
print(f"Srednja potrošnja: {mpg_mean:.2f} mpg")

# e) Isti izračun, ali samo za automobile s 6 cilindara
mpg_6cyl = mpg[cyl == 6]

mpg_min_6cyl = np.min(mpg_6cyl)
mpg_max_6cyl = np.max(mpg_6cyl)
mpg_mean_6cyl = np.mean(mpg_6cyl)

print("\nZa automobile s 6 cilindara:")
print(f"Minimalna potrošnja: {mpg_min_6cyl} mpg")
print(f"Maksimalna potrošnja: {mpg_max_6cyl} mpg")
print(f"Srednja potrošnja: {mpg_mean_6cyl:.2f} mpg")
