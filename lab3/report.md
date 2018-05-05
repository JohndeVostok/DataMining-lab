# Data Mining Report 3

计54 马子轩 2015012283

## 数据立方体

### Star schema

fact_table: [date_key, spectator_key, location_key, game_key|count, charge]

date: [date_key, day_of_week, day, month, year]

spectator: [spectator_key]

location: [location_key, street, city, province, country]

game: [game_key, game_name, game_type]

measures: [count, charge]

### OLAP

针对game进行drill_up操作从key至any.

针对date进行drill_up操作,从key至year.

切块:取spectator=“学生”, location="清华大学大礼堂",date="2018",game="any"

先针对限定条件对层进行调整.对date和game进行上卷.再进行切块.即得到需要的数据.

## 频繁项集与关联规则

|TID|Items|
|-|-|
|T01|{K, A, D, B}|
|T02|{D, A, C, E, B}|
|T03|{C, A, B, E}|
|T04|{B, A, D}|

对每个候选计数

{A:4, B:4, C:2, D:3, E:2, K:1} -> {A:4, B:4, C:2, D:3, E:2}

{AB:3, AC:1, AD:3, AE:2, BC:2, BD:3, BE:2, CD:1, CE:2, DE:1} -> {AB:3, AD:3, AE:2, BC:2, BD:3, BE:2, CE:2}

{ABD:3, ABE:2, BCE:2}

{ABDE: 1, ABCE:2} -> {ABCE:2}

因此含E的频繁项集为{E, AE, BE, CE, ABE, BCE, ABCE}

查询关联规则buy(x)&buy(y)->buy(z)

查看3-频繁项集

ABD, ABE, BCE

count(ABD)/count(AB) = 3 / 3 = 1 A&B->D

count(ABD)/count(AD) = 3 / 3 = 1 A&D->B

count(ABD)/count(BD) = 3 / 3 = 1 B&D->A

count(ABE)/count(AB) = 2 / 3 = 0.66

count(ABE)/count(AE) = 2 / 2 = 1 A&E->B

count(ABE)/count(BE) = 2 / 2 = 1 B&E->A

count(BCE)/count(BC) = 2 / 2 = 1 B&C->E

count(BCE)/count(BE) = 2 / 2 = 1 B&E->C

count(BCE)/count(CE) = 2 / 2 = 1 C&E->B

因此关联规则有

A&B->D

A&D->B

A&E->B

B&C->E

B&D->A

B&E->A

B&E->C

C&E->B

### 约束的性质

|Constraint|Antimonotone|Monotone|Succinct|
|-|-|-|-|
|$0\notin S$|T|F|T|
|$S中的正数数量大于5$|F|T|weak|
|$S中只包含3的倍数$|T|F|T|
|$min(S)>0, max(S)<10$|T|F|T|
|$S的方差小于1$|F|F|F|

