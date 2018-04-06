from matplotlib import pyplot as plt
import pickle
import math

with open("attr.pkl", "rb") as f:
    attrList = pickle.load(f)

# Histogram

# tags

tagMap = {}
tagList = []
tagNum = []

for i in attrList:
    tags = i["tags"]
    for j in tags:
        if not j in tagMap:
            tagMap[j] = len(tagList)
            tagList.append(j)
            tagNum.append(0)
        tagNum[tagMap[j]] += 1

plt.figure(0)
plt.figure(figsize = (12, 8))
plt.bar(tagList, tagNum)
plt.savefig("tags.png")
plt.close(0)

