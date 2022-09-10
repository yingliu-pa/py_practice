# req: 提取表格，包含以下变量：来源篇名，来源作者，期    刊，第一机构，年代卷期，关 键 词

import re
import pandas as pd

categories = ["来源篇名", "来源作者", "期    刊", "第一机构", "年代卷期", "关 键 词"]

raw_file_path = "./jingfu.txt"

with open(raw_file_path, "r") as f:
    raw_data = f.readlines()

# step 1. clean data
datas = []
article = []
for line in raw_data:
    line = line.strip()  # 去除行尾的回车
    if "----" in line:
        datas.append(article)
        article = []
    else:
        article.append(line)

result_data = []
# step 2. mining information
reg = re.compile(r"^【(.*)】(.*)$")
for clean_article in datas:
    article_info = {}
    for line in clean_article:
        reg_results = re.findall(reg, line)
        if len(reg_results) > 0:
            category, text = reg_results[0]
            if category in categories:
                article_info[category] = text
    result_data.append(article_info)

# step 3. write result to csv
save_path = "./jingfu.csv"
infos = pd.DataFrame(result_data, columns=categories)
# infos.to_csv(save_path, index=False, encoding="utf-8", sep="\t")
infos.to_excel("./result2.xls", index=False) #第40行是生成CSV文件，用MS excel打开会乱码
