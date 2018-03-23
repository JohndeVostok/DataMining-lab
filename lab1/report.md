# Data Mining Report 1

计54 马子轩

## 数据属性类型练习

对于下面列出的每一个数据属性，从 {Nominal, Ordinal, Interval, Ratio} 四个选
项中选出最合适的类型，并说明理由。
军人的军衔 Ordinal 能排序，不能加减
IP地址 Nominal 地址排序加减都没有意义
程序的运行时间 Ratio 0是有意义的
人的出生日期 Interval 0是没有意义的
使用的编程语言 Nominal 没啥可说的
发表的论文数量 Ratio 没发就是没发

## 计算统计信息

1、假定用于分析的数据为某食品中的脂肪含量。样本的值分别是

|脂肪(%)|9.5|26.5|7.8|17.8|31.4|25.9|27.4|27.2|31.2|
|--|--|--|--|--|--|--|--|--|--|
|脂肪(%)|34.6|42.5|28.8|33.4|30.2|34.1|32.9|41.2|35.7|


计算这组数据的均值、中位数和众数

均值:28.78

中位数:30.7

众数:都不一样， 全都是众数

2、给出五数概括，并画出盒图

min:7.8

Q1:26.5

Q2:30.7

Q3:34.1

max:42.5

IQR = 7.6



min 15.1

max 45.5

离群点 7.8 9.5

盒: 15.1 - 42.5

##文本数据的表示

1、根据语料内容构造词典，然后将语料中的每篇文档都表示成词典上的 tf-idf 向量。

见代码data.py tf_idf.py

实际过程，就是使用正则表达式进行替换，然后构造词典

data.py

```python
import re
import pickle
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
	pickle.dump((wordCount, data), f)
```

根据定义计算tf-idf

tf_idf.py

```python
import re
import pickle
import numpy as np

NFILE = 300

with open("data.pkl", "rb") as f:
    (wordCount, data) = pickle.load(f)

nWord = len(data)

idf = np.zeros((nWord, ), dtype = float)
tf = np.zeros((nWord, NFILE), dtype = float)
tf_idf = np.zeros((nWord, NFILE), dtype = float)
wordList = []

for idx, word in enumerate(data):
    wordList.append(word)
    for p in data[word]:
        tf[idx][p[0]] = float(p[1]) / wordCount[p[0]]
        idf[idx] += 1

for index in range(idf.shape[0]):
    idf[index] = np.log(NFILE / (1 + idf[index]))

for wid in range(tf.shape[0]):
    for fid in range(tf.shape[1]):
        tf_idf[wid][fid] = tf[wid][fid] * idf[wid]

with open("tf_idf.pkl", "wb") as f:
    pickle.dump(tf_idf, f)
```

根据定义构造共现矩阵

common.py

```python
import re
import pickle
import numpy as np

NFILE = 300

with open("data.pkl", "rb") as f:
    (wordCount, data) = pickle.load(f)

nWord = len(data)
common = np.zeros((nWord, ), dtype = int)

values = list(data.values())

with open("common.txt", "w") as f:
    for wid1 in range(nWord):
        for wid2 in range(nWord):
            common[wid2] = 0
            m = len(values[wid1])
            n = len(values[wid2])
            i = 0
            j = 0
            while (i < m and j < n):
                if (values[wid1][i][0] < values[wid2][j][0]):
                    i += 1
                    continue
                if (values[wid1][i][0] > values[wid2][j][0]):
                    j += 1
                    continue
                if (values[wid1][i][0] == values[wid2][j][0]):
                    common[wid2] += 1
                    i += 1
                    j += 1
        f.writelines([" ".join([str(i) for i in common.tolist()]) + '\n'])
        if (wid1 % 1024 == 0):
            print("{}/{} finish.".format(wid1, nWord))

print("all finished.")
```

根据tf-idf计算欧几里得距离和余弦距离

以下为计算结果，我认为，这种判断文章特征的方式，不是很好。但可能因为语料中可以文章相似度本身就不高，而且语料过少，导致结果可验证性不高。

tf_idf_file.py

```python
import pickle
import numpy as np

NFILE = 300

with open("tf_idf.pkl", "rb") as f:
    tf_idf = pickle.load(f)

eDist = np.zeros((NFILE, ), dtype = float)
cDist = np.zeros((NFILE, ), dtype = float)

p = 0.
for wid in range(tf_idf.shape[0]):
    p += tf_idf[wid][0] ** 2
p = p ** 0.5

for fid in range(NFILE):
    tmp = 0.
    for wid in range(tf_idf.shape[0]):
        eDist[fid] += (tf_idf[wid][fid] - tf_idf[wid][0]) ** 2
        cDist[fid] += tf_idf[wid][fid] * tf_idf[wid][0]
        tmp += tf_idf[wid][fid] ** 2
    tmp = tmp ** 0.5
    eDist[fid] = eDist[fid] ** 0.5
    cDist[fid] = 1 - cDist[fid] / (p * tmp)

eSorted = zip(list(eDist), range(NFILE))
cSorted = zip(list(cDist), range(NFILE))

eSorted = sorted(eSorted)
cSorted = sorted(cSorted)

print("Edist:")
for i in range(10):
    print(eSorted[i][0], eSorted[i][1])

print("Cdist:")
for i in range(10):
    print(cSorted[i][0], cSorted[i][1])
```

```shell
$ python3 tf_idf_file.py                        [17:53:29]
Edist:
0.0 0
0.24696714427274583 212
0.2485646688261493 256
0.2488437486558295 52
0.24895389305724583 31
0.24967582907115227 215
0.25128178748885976 258
0.25657015923763843 27
0.256751467939199 194
0.25706365909906465 103
Cdist:
0.0 0
0.8887202110111273 43
0.912349188122086 37
0.9165169730448317 293
0.9172469272038375 51
0.9289332347647055 196
0.9294895238821987 151
0.9309250647439964 148
0.9379042126445368 129
0.9380074487650352 238
```

利用共现矩阵计算欧几里得距离和余弦距离

以下为计算结果，因为python实在太慢了，我不得不使用c++。事实证明，python看起来完成不了的任务，c++几秒钟就搞定了。结果上来看，两种距离的结论类似，但是不得不说的是，perhaps和kid,platform真的没什么关系。所以这种算法实际使用效果也不好，不能像w2v那样精确的找出相关词语。

common.cpp

```cpp
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>

const int nword = 11691;

int c[nword][nword];
float a[nword], b[nword];

struct dist{
	int a;
	float b, c;
} f[nword];

bool cmp1(const dist &a, const dist &b){
	return a.b < b.b;
}

bool cmp2(const dist &a, const dist &b){
	return a.c > b.c;
}

int main(){
	freopen("common.txt", "r", stdin);
	setvbuf(stdin, 0, _IOFBF, 0xffff);
	for (int i = 0; i < nword; i++){
		for (int j = 0; j < nword; j++)
			scanf("%d", &c[i][j]);
		if (!(i & 0xff)) printf("%d/%d\n", i, nword);
	}
	float p = 0, tmp = 0;
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	for (int i = 0; i < nword; i++) p += c[0][i] * c[0][i];
	for (int i = 0; i < nword; i++){
		tmp = 0;
		for (int j = 0; j < nword; j++){
			a[i] += (c[i][j] - c[0][j]) * (c[i][j] - c[0][j]);
			b[i] += c[i][j] * c[0][j];
			tmp += c[i][j] * c[i][j];
		}
		a[i] = sqrt(a[i]);
		b[i] = b[i] / (sqrt(p) * sqrt(tmp));
		if (!(i & 0xff)) printf("%d/%d\n", i, nword);
	}
	for (int i = 0; i < nword; i++){
		f[i].a = i;
		f[i].b = a[i];
		f[i].c = b[i];
	}
	std::sort(f, f + nword, cmp1);
	printf("Edist\n");
	for (int i = 0; i < 10; i++) printf("%d %.5lf\n", f[i].a, f[i].b);
	std::sort(f, f + nword, cmp2);
	printf("Cdist\n");
	for (int i = 0; i < 10; i++) printf("%d %.5lf\n", f[i].a, f[i].c);
	return 0;
}
```

```shell
Edist
0 0.00000
103 25.39685
128 25.61250
5 26.64582
755 28.17801
35 29.30870
8986 29.84962
1237 29.86637
5732 29.93326
5771 30.29852
Cdist
0 1.00000
5 0.75890
103 0.75407
128 0.74806
80 0.73913
75 0.73761
122 0.73617
459 0.73583
498 0.73520
23 0.73420
```

## 实验总结

经过这个小实验，简单了解了词袋模型的使用情况，亲身体验了这种模型不靠谱的地方，为后续学习打下了坚实的基础，并让我对后续的文本处理算法有了更多的兴趣。
