from mymodule import say_hi,__version__

# 如果导入的模块中已有__version__这一名称，就会产生冲突，因此推荐使用 from mymodule import 这种形式
say_hi()
print('Version', __version__)