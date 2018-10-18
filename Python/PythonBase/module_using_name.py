# 每个模块都有一个名称，而模块中的语句可以找到它们所处模块的名称
# 这对于确定模块是独立运行还是被导入进来运行的这一特定目的来说大为有用
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
