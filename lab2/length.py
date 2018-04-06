from matplotlib import pyplot as plt
import pickle

with open("attr.pkl", "rb") as f:
    attrList = pickle.load(f)

# Histogram

# length of word

lenNum = []
for i in range(30):
    lenNum.append(0)

for i in attrList:
    for j in i["stems"]:
        lenNum[len(j)] += 1

plt.figure(0)
plt.figure(figsize = (12, 8))
plt.bar(range(len(lenNum)), lenNum)
plt.savefig("length.png")
plt.close(0)
