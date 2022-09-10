import os
import pandas as pd

#将文件读取出来放一个列表里
pwd = "/Users/yingliu/Desktop/Meta/0304"
#新建列表存放每个文件数据（依次读取多个相同结构的excel文件并创建dataframe
dfs=[]
for root, dirs, files in os.walk(pwd): #第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件
	for file in files:
		file_path = os.path.join(root, file)
		print(file_path) #print结果发现有一个.DS_Store的隐藏文件，所以xlrd读不出来会报错
		if "xls" in file_path: #xlrd读不了隐藏文件的解决办法是加一个判断
			df = pd.read_excel(file_path)
			dfs.append(df)
df = pd.concat(dfs)
df.to_excel("/Users/yingliu/Desktop/Meta/0304/result.xls", index=False)


"""
WOS 搜索语法
SO=(Public Administration Review) OR 
SO=(Journal of Public Administration Research and Theory) OR 
SO=(Public Management Review) OR 
SO=(International Journal of Public Administration) OR 
SO=(International Public Management Journal) OR 
SO=(Public Administration) OR 
SO=(Governance-An International Journal of Policy Administration and Institution) OR 
SO=(International Review of Administrative Science) OR 
SO=(Journal of Human Resources) OR 
SO=(Administrative Science Quarterly) OR 
SO=(American Review of Public Administration) OR 
SO=(Review of Public Personnel Administration) OR 
SO=(Local Government Studies) OR 
SO=(Social Policy & Administration) OR 
SO=(Public Policy and Administration) OR 
SO=(Nonprofit Management & Leadership) OR 
SO=(Administration & Society)
"""
