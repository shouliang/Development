# 日常应用比较广泛的模块
# 1. 文字处理 re
# 2. 日期类型time、datetime
# 3. 数学 math random
# 4. 文件和目录 path lib os.path
# 5. 数据压缩和归档tarfile
# 6. 通常操作系统 os logging argparse
# 7. 多线程 threading queue
# 8. Internet数据处理 base64、json、urllib
# 9. 结构化标记处理工具 html、xml
# 10. 开发工具的unitest
# 11. 调试工具的 timeit
# 12. 软件包的发布 venv
# 13. 运行服务的 __main__

import re

p = re.compile('a')
print(p.match('a'))

p = re.compile('ca*t')
print(p.match('cat'))

# .匹配单个字符
p = re.compile('.')
print(p.match('b'))

p = re.compile('...')
print(p.match('rfd'))

# ^ 以某开始  $以某结尾

# * 匹配0次或者多次  + 一次或者多次 ?0次或者1次

#  {m}出现m次 ,{m,n}匹配m到n次
p = re.compile('ca{4}t')
print(p.match('caaaat'))

# []  匹配中括号中任意一个
# | 匹配左边或右边
# \d数字 [0-9]+ \D非数字

#^$ 匹配空行
# .*? 不使用贪婪模式  abccccccd abc*d

