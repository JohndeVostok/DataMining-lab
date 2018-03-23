import numpy as np
import pickle

nWord = 11691

with open("common.txt", "r") as f:
    data = np.array([[int(j) for j in i.split()] for i in f.readlines()], dtype=int)

print(data.shape)
