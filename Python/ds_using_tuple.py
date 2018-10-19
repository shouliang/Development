# 元组类似于字符串，是不可改变的
# 空的元组如：myempty = ()
# 但是只拥有一个项目的元组，必须在第一个项目后面加上一个逗号，否则Python不能识别出是一个元组还是一个被括号所环绕的对象
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

# 元组可以不使用括号，但不推荐
new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)

print('Animals brought from old zoo are', new_zoo[2])
print('Last animals brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo) - 1 + len(new_zoo[2]))
