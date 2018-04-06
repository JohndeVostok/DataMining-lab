import pickle

with open("attr.pkl", "rb") as f:
    attrList = pickle.load(f)

# Bag of words

bow = []

for i in attrList:
    bow.append({})
    for j in i["stems"]:
        if not hash(j) in bow[-1]:
            bow[-1][hash(j)] = 0
        bow[len(bow) - 1][hash(j)] += 1
