import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

# 绘制简单的曲线
# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()

# x = np.linspace(-np.pi, np.pi, 100)  # x轴的定义域为 -3.14到3.14，中间间隔100个元素
# plt.plot(x, np.sin(x))
# plt.show()

# x = np.linspace(-np.pi * 2, np.pi * 2, 100)  # x轴的定义域为 -2pi到2pi，中间间隔100个元素
# plt.figure(1, dpi=50)  # 创建图表
# for i in range(1, 5):  # 绘制多条
#     plt.plot(x, np.sin(x / i))
# plt.show()


# x = np.linspace(-np.pi * 2, np.pi * 2, 100)  # x轴的定义域为 -2pi到2pi，中间间隔100个元素
# data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
# plt.hist(data)  # 直方图
# plt.show()

# 散点图
# x = np.arange(1, 10)
# y = x
# fig = plt.figure()
# plt.scatter(x, y, c='r', marker='o')  # 'r'散点的颜色为红色，marker表示指定散点图形状为圆形
# plt.show()

# 使用pandas
# iris = pd.read_csv('./iris_training.csv')
# print(iris.head())
#
# iris.plot(kind="scatter", x="120", y="4")
# plt.show()

# seaborn美观点

# iris = pd.read_csv('./iris_training.csv')
# # 设置样式
# sns.set(style='white', color_codes=True)
# # 设置绘制格式为散点图
# sns.jointplot(x="120", y="4", data=iris, size=5)
# # distplot绘制曲线
# sns.distplot(iris['120'])
# plt.show()

# 不同颜色的划分
# FacetGrid 一般绘图函数
# hue 彩色显示分类0/1/2
# plt.scatter 绘制散点图
# add_legend 显示分类的描述信息
iris = pd.read_csv('./iris_training.csv')
# 设置样式
sns.set(style='white', color_codes=True)
# sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "120", "4").add_legend()

sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "setosa", "versicolor").add_legend()
plt.show()
