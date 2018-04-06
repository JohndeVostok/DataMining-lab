from matplotlib import pyplot as plt
import pickle
import math

with open("attr.pkl", "rb") as f:
    attrList = pickle.load(f)

# Histogram

# binning

wordNum = []

width = 423

widthLabel = []
widthList = []
depthLabel = []
depthList = []

for i in range(10):
    widthLabel.append(str(i * width) + "-" + str((i + 1) * width - 1))
    widthList.append(0)
    depthList.append(50)

for i in attrList:
    length = len(i["stems"])
    wordNum.append(length)
    widthList[math.floor(length / width)] += 1;

wordNum.sort()

for i in range(10):
    depthLabel.append(str(wordNum[i * 50]) + "-" + str(wordNum[(i + 1) * 50 - 1]))

plt.figure(0)
plt.figure(figsize = (12, 8))
plt.bar(widthLabel, widthList)
plt.savefig("widthBin.png")
plt.close(0)

plt.figure(1)
plt.figure(figsize = (12, 8))
plt.bar(depthLabel, depthList)
plt.savefig("depthBin.png")
plt.close(1)
