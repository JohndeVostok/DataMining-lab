def cla(idx):
	a = (p[idx][0] - q[0][0]) ** 2 + (p[idx][1] - q[0][1]) ** 2
	b = (p[idx][0] - q[1][0]) ** 2 + (p[idx][1] - q[1][1]) ** 2
	if (a < b):
		return 0
	else:
		return 1

def ret():
	s = [[0, 0], [0, 0]]
	t = [0, 0]
	for i in range(13):
		s[c[i]][0] += p[i][0]
		s[c[i]][1] += p[i][1]
		t[c[i]] += 1
	s[0][0]/=t[0]
	s[0][1]/=t[0]
	s[1][0]/=t[1]
	s[1][1]/=t[1]
	return s

if __name__ == "__main__":
	p = [(1,3), (1,2), (2,1), (2,2), (2,3), (3,2), (5,3), (4,3), (4,5), (5,4), (5,5), (6,4), (6,5)]
	q = [(0,4),(6,5)]

	c = [cla(i) for i in range(13)]
	q = ret()
	print(c)
	print(q)

	c = [cla(i) for i in range(13)]
	q = ret()
	print(c)
	print(q)
	c = [cla(i) for i in range(13)]
	q = ret()
	print(c)
	print(q)

