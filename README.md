# py_practice

## 1. text to excel
提取表格，包含以下变量：来源篇名，来源作者，期    刊，第一机构，年代卷期，关 键 词
- step 0: clean data
- step 1: mining information
- step 2: write results to csv/excel

```
import re
import pandas as pd
```
---

## 2. merge excel
WOS一个页面只能下载500篇文献，将15个excel表格合并成一个
```
import os
import pandas as pd
```
.DS_Store 是OS系统下的隐藏文件，xlrd在读文件夹中的excel表格时，因为读不出来会报错，需要加一个判断

```
		if "xls" in file_path: #xlrd读不了隐藏文件的解决办法是加一个判断
			df = pd.read_excel(file_path)
			dfs.append(df)
```
---

## 3. frequency
计算7500篇文献的关键词词频
- step 0: 读取excel文件
- step 1: 获取value （对于关键词列无数据的观测值，用另外一列的值补全）
- step 2: 分割并统计
- step 3: 对结果排序
- step 4: 输出结果

```
import xlrd
from collections import Counter
from operator import itemgetter
```

