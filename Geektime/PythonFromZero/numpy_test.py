import numpy as np

# 数组和数据类型
arr1 = np.array([2, 3, 7])
print(arr1.dtype)

arr2 = np.array([1.3, 4.6, 5.1])
print(arr2.dtype)

print(arr1 + arr2)

# 标量
print(arr2 * 10)

data = [[1, 2, 3], [4, 5, 6]]
arr3 = np.array(data)
print(arr3)
print(arr3.dtype)

# 矩阵置为0 或者 1
print(np.zeros((3, 5)))
print(np.ones((4, 6)))

# empty 会填充随机值
print(np.empty((5, 6)))

# 切片
print(np.arange(10))
arr4 = np.arange(10)
print(arr4[5])
print(arr4[5:8])
arr4[5:8] = 10  # 切片直接赋值
print(arr4)

arr_slice = arr4[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr4)
