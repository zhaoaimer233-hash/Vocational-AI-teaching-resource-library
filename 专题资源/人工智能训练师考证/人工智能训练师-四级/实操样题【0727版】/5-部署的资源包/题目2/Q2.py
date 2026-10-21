import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据集
data = pd.<1>(<2>)

# 数据预处理
# 查找缺失值
print('数据集中的缺失值数量：\n', data.<3>.sum())

# 处理缺失值
data = data.dropna()  # 删除含有缺失值的行

# 查找和处理重复值
print('数据集中的重复值数量：', data.<4>.sum())
data = data.drop_duplicates()  # 删除重复值

# 查找和处理异常值
Q1 = data['G3'].quantile(0.25)
Q3 = data['G3'].quantile(0.75)
IQR = Q3 - Q1
outlier = data[(data['G3'] < Q1 - 1.5*IQR) | (data['G3'] > Q3 + 1.5*IQR)]
print('数据集中的异常值数量：', len(<5>))
data = data[(data['G3'] >= Q1 - 1.5*IQR) & (data['G3'] <= Q3 + 1.5*IQR)]  # 删除异常值

# 显示前五行数据
print('处理后的前五行数据：\n', data.<6>)

# 数据分析和可视化
# 分析成绩分布并绘制柱状图
plt.<8>(<7>['G3'], bins=20)
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Score Distribution')
plt.show()

# 分析年龄属性并绘制箱线图
sns.<9>(x=<10>, y='G3', data=data)
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Age Distribution')
plt.show()

# 计算相关性系数
corr = data.<11>['G3'].sort_values(ascending=False)
print('数据集中各数据与学生成绩的相关性系数：\n', corr)

# 选择相关度系数最高的前五个特征
top_five_features = corr.<12>[:5]

# 创建一个新的DataFrame，只包含这五个特征
top_five_data = data[top_five_features]

# 计算这五个特征之间的相关性
top_five_corr = top_five_data.corr()

# 绘制热力图
fig, ax = plt.subplots(figsize=(10, 8))
sns.<13>(top_five_corr, annot=True, cmap='coolwarm', ax=ax)
plt.title('Correlation Heatmap')
plt.show()
