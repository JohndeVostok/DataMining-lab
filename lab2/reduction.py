import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

with open("100_word_vector.txt", "r") as f:
    content = f.read()

cList = content.split()

wordList = []
vectorList = []

idx = 0
for i in range(100):
    wordList = cList[idx]
    idx += 1
    vectorList.append([])
    for j in range(100):
        vectorList[i].append(cList[idx])
        idx += 1

vec = np.array(vectorList)

pcaList = PCA(n_components = 2).fit_transform(vec)
tsneList = TSNE(n_components = 2).fit_transform(vec)

pcax = pcaList[:, 0]
pcay = pcaList[:, 1]

plt.figure(0)
plt.figure(figsize = (12, 8))
plt.scatter(pcax, pcay)
plt.savefig("pca.png")
plt.close(0)

tsnex = tsneList[:, 0]
tsney = tsneList[:, 1]

plt.figure(1)
plt.figure(figsize = (12, 8))
plt.scatter(tsnex, tsney)
plt.savefig("tsne.png")
plt.close(1)

