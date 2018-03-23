import pickle
import numpy as np

NFILE = 300

with open("tf_idf.pkl", "rb") as f:
    tf_idf = pickle.load(f)

eDist = np.zeros((NFILE, ), dtype = float)
cDist = np.zeros((NFILE, ), dtype = float)

p = 0.
for wid in range(tf_idf.shape[0]):
    p += tf_idf[wid][0] ** 2
p = p ** 0.5

for fid in range(NFILE):
    tmp = 0.
    for wid in range(tf_idf.shape[0]):
        eDist[fid] += (tf_idf[wid][fid] - tf_idf[wid][0]) ** 2
        cDist[fid] += tf_idf[wid][fid] * tf_idf[wid][0]
        tmp += tf_idf[wid][fid] ** 2
    tmp = tmp ** 0.5
    eDist[fid] = eDist[fid] ** 0.5
    cDist[fid] = 1 - cDist[fid] / (p * tmp)

eSorted = zip(list(eDist), range(NFILE))
cSorted = zip(list(cDist), range(NFILE))

eSorted = sorted(eSorted)
cSorted = sorted(cSorted)

print("Edist:")
for i in range(10):
    print(eSorted[i][0], eSorted[i][1])

print("Cdist:")
for i in range(10):
    print(cSorted[i][0], cSorted[i][1])

