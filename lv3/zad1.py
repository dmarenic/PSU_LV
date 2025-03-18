import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Učitavanje skupa podataka mtcars
mtcars = pd.read_csv("mtcars.csv")

# Postavljanje naziva automobila kao indeksa
mtcars.index = mtcars["car"]
del mtcars["car"]

# 1. Kojih 5 automobila ima najveću potrošnju?
print(mtcars.sort_values(by="mpg", ascending=True).head(5))

# 2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
print(mtcars[mtcars["cyl"] == 8].sort_values(by="mpg", ascending=True).head(3))

# 3. Kolika je srednja potrošnja automobila sa 6 cilindara?
print(mtcars[mtcars["cyl"] == 6]["mpg"].mean())

# 4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
print(mtcars[(mtcars["cyl"] == 4) & (mtcars["wt"] * 1000 >= 2000) & (mtcars["wt"] * 1000 <= 2200)]["mpg"].mean())

# 5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem?
print(mtcars["am"].value_counts())

# 6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 KS?
print(len(mtcars[(mtcars["am"] == 0) & (mtcars["hp"] > 100)]))

# 7. Kolika je masa svakog automobila u kg?
mtcars["wt_kg"] = mtcars["wt"] * 453.592
print(mtcars["wt_kg"])

