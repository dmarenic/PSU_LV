import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Učitavanje skupa podataka mtcars
mtcars = pd.read_csv("mtcars.csv")

# 1. Barplot potrošnje automobila s 4, 6 i 8 cilindara
mtcars.groupby("cyl")["mpg"].mean().plot(kind='bar', title="Potrošnja po broju cilindara")
plt.xlabel("Broj cilindara")
plt.ylabel("mpg")
plt.show()

# 2. Boxplot distribucije težine automobila s 4, 6 i 8 cilindara
mtcars.boxplot(column="wt", by="cyl")
plt.xlabel("Broj cilindara")
plt.ylabel("Težina (1000 lbs)")
plt.title("Distribucija težine automobila")
plt.suptitle("")
plt.show()

# 3. Potrošnja automobila s ručnim i automatskim mjenjačem
mtcars.boxplot(column="mpg", by="am")
plt.xticks([1, 2], ["Automatski", "Ručni"])
plt.xlabel("Vrsta mjenjača")
plt.ylabel("Potrošnja (mpg)")
plt.title("Usporedba potrošnje po tipu mjenjača")
plt.suptitle("")
plt.show()

# 4. Odnos ubrzanja i snage automobila po tipu mjenjača
colors = mtcars["am"].map({0: "blue", 1: "red"})
plt.scatter(mtcars["hp"], mtcars["qsec"], c=colors)
plt.xlabel("Snaga (KS)")
plt.ylabel("Ubrzanje (s)")
plt.title("Odnos snage i ubrzanja po tipu mjenjača")
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Automatski'),
                    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Ručni')])
plt.show()