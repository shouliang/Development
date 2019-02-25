import os

# os.path
# 绝对路径
print(os.path.abspath('.'))
print(os.path.abspath('..'))

print(os.path.exists('/Users'))

print(os.path.isdir('/Users'))
print(os.path.isfile('/Users'))

# 连接路径
# os.path.join('/tmp/a','b')


print('------------')
# pathlib 简单使用
from pathlib import Path

p = Path('.')
print(p.resolve())  # 绝对路径
print(Path.is_dir(Path('/User')))

# 新建目录
q = Path('./tmp')
Path.mkdir(q, parents=True)
