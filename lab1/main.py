import re

NFILE = 300

data = {}

for index in range(NFILE):

	with open("nyt_corp0/{}".format(index), "r") as f:
		text = f.read()
		text = re.sub("[^a-zA-Z]+", " ", text).lower().split();

	for word in text:
		if not word in data:
			data[word] = [[index, 0]]
		if (data[word][-1][0] != index):
			data[word].append([index, 0])
		data[word][-1][1] += 1;

with open("sb.out", "w") as f:
	f.write(str(data))
