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
