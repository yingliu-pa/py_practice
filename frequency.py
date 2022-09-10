import xlrd
from collections import Counter
from operator import itemgetter

# step 0. 读excel文件
file_path = "./Book6.xlsx"
table = xlrd.open_workbook(file_path).sheets()[0] # 读取表
nrow, ncol = table.nrows, table.ncols # 记录行数和列数，第一行是表头

results = Counter()
# 对每行处理
for index in range(1, nrow): #第0行是表头
	# step 1. 获取value
	value = table.cell_value(index, 0) #index是行的参数（第12行），0是指表格的第一列
	if value == "":
	# 如果为空，则取Keywords Plus列的值
		value = table.cell_value(index, 1)
	# step 2. 分割并统计
	keywords = []
	for word in value.split(";"):
		if word.strip() != "":
			keywords.append(word.strip().lower())
	# keywords = [word.strip().lower() for word in value.split(";") if word.strip() != ""] #这一行可以代替第19-22行，是一样的效果，这一行代码更简洁且更高级
	results.update(keywords)

# step 3. 对结果排序
ordered_results = sorted([(key, value) for key, value in results.items()], key=itemgetter(1), reverse=True) #（key 和reverse是sorted函数的参数，如果key=itemgetter(0), 那么就是按照关键词的首字母进行排序）

# step 4. 输出结果
save_file_path = "./frequency.txt"
with open(save_file_path, "w") as f:
	for key, value in ordered_results:
		f.write(f"{key} : {value}\n")