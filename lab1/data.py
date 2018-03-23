import re
import cPickle
import numpy as np

NFILE = 300

data = {}

wordCount = np.zeros((NFILE, ), dtype = int)

for index in range(NFILE):

	with open("nyt_corp0/{}".format(index), "r") as f:
		text = f.read()
		text = re.sub("[^a-zA-Z]+", " ", text).lower().split();

	wordCount[index] = len(text)

	for word in text:
		if not word in data:
			data[word] = [[index, 0]]
		if (data[word][-1][0] != index):
			data[word].append([index, 0])
		data[word][-1][1] += 1;

with open("data.pkl", "wb") as f:
	cPickle.dump((wordCount, data), f)
