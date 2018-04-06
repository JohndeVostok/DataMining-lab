from matplotlib import pyplot as plt
import pickle
import math

with open("attr.pkl", "rb") as f:
    attrList = pickle.load(f)

# Histogram

# date

dateMap = {}
dateList = []
dateNum = []

for i in attrList:
    date = i["date"]
    strDate = date.strftime("%Y-%m")
    if not strDate in dateMap:
        dateMap[strDate] = len(dateList)
        dateList.append(strDate)
        dateNum.append(0)
    dateNum[dateMap[strDate]] += 1

plt.figure(0)
plt.figure(figsize = (12, 8))
plt.bar(dateList, dateNum)
plt.savefig("date.png")
plt.close(0)
