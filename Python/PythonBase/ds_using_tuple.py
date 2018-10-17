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