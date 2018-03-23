import re
import pickle
import numpy as np

NFILE = 300

with open("data.pkl", "rb") as f:
    (wordCount, data) = pickle.load(f)

nWord = len(data)
common = np.zeros((nWord, ), dtype = int)

values = list(data.values())

with open("common.txt", "w") as f:
    for wid1 in range(nWord):
        for wid2 in range(nWord):
            common[wid2] = 0
            m = len(values[wid1])
            n = len(values[wid2])
            i = 0
            j = 0
            while (i < m and j < n):
                if (values[wid1][i][0] < values[wid2][j][0]):
                    i += 1
                    continue
                if (values[wid1][i][0] > values[wid2][j][0]):
                    j += 1
                    continue
                if (values[wid1][i][0] == values[wid2][j][0]):
                    common[wid2] += 1
                    i += 1
                    j += 1
        f.writelines([" ".join([str(i) for i in common.tolist()]) + '\n'])
        if (wid1 % 1024 == 0):
            print("{}/{} finish.".format(wid1, nWord))

print("all finished.")
