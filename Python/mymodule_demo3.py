from mymodule import *

# import * 会导入公共名称，但是不会导入__version__名称，因为它以双下划线开头
say_hi()
print('Version', __version__)