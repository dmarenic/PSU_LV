import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage


def generate_data(n_samples, flagc):
    if flagc == 1:
        random_state = 365
        X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
    elif flagc == 2:
        random_state = 148
        X, y = make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
    elif flagc == 3:
        random_state = 148
        X, y = make_blobs(n_samples=n_samples, centers=4, cluster_std=[1.0, 2.5, 0.5, 3.0], random_state=random_state)
    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    else:
        X = []
        y = []
    return X, y


X, y = generate_data(500, flagc=5)


Z = linkage(X, method='ward') 


plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Dendogram - Hijerarhijsko grupiranje')
plt.xlabel('Podaci')
plt.ylabel('Udaljenost')
plt.show()
#Dendogram prikazuje kako se pojedini podaci spajaju u grupe na temelju njihove slicnosti