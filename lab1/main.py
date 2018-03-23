import re
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

nWord = len(data)

idf = np.zeros((nWord, ), dtype = float)
tf = np.zeros((nWord, NFILE), dtype = float)
tf_idf = np.zeros((nWord, NFILE), dtype = float)
common = np.zeros((nWord, nWord), dtype = int)
wordList = []

idx = 0

for word in data:
	wordList.append(word)
	for p in data[word]:
		tf[idx][p[0]] = float(p[1]) / wordCount[p[0]];
		idf[idx] += 1;
	idx += 1

for index in range(idf.shape[0]):
	idf[index] = np.log(NFILE / (1 + idf[index]))

for wid in range(tf.shape[0]):
	for fid in range(tf.shape[1]):
		tf_idf[wid][fid] = tf[wid][fid] * idf[wid];

for wid1 in range(tf.shape[0]):
	for wid2 in range(tf.shape[0]):
		for fid in range(tf.shape[1]):
			if (tf[wid1][fid] > 0 and tf[wid2][fid] > 0):
				common[wid1][wid2] += 1


