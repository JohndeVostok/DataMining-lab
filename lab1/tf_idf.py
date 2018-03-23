import re
import pickle
import numpy as np

NFILE = 300

with open("data.pkl", "rb") as f:
    (wordCount, data) = pickle.load(f)

nWord = len(data)

idf = np.zeros((nWord, ), dtype = float)
tf = np.zeros((nWord, NFILE), dtype = float)
tf_idf = np.zeros((nWord, NFILE), dtype = float)
wordList = []

for idx, word in enumerate(data):
    wordList.append(word)
    for p in data[word]:
        tf[idx][p[0]] = float(p[1]) / wordCount[p[0]]
        idf[idx] += 1

for index in range(idf.shape[0]):
    idf[index] = np.log(NFILE / (1 + idf[index]))

for wid in range(tf.shape[0]):
    for fid in range(tf.shape[1]):
        tf_idf[wid][fid] = tf[wid][fid] * idf[wid]

with open("tf_idf.pkl", "wb") as f:
    pickle.dump(tf_idf, f)
