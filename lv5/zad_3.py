from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
# Umjetni podaci
df = pd.read_csv('occupancy_processed.csv')


scaler = StandardScaler()
scaled_data = scaler.fit_transform(df) 
# Kreiraj i istreniraj stablo odlucivanja


#X = df.iloc[:, 0:-1]
#y = df.iloc[:, -1]
X = scaled_data.iloc[:, 0:-1]
print(X)
y = scaled_data.iloc[:, -1]
dt = DecisionTreeClassifier(max_depth=2)
dt.fit(X, y)
# Predikcija modela
y_pred = dt.predict(X)
# Vizualizacija stabla odlucivanja
plt.figure(figsize=(12, 8))
plot_tree(dt, filled=True)
plt.show()