# 集合是简单对象的无序集合，涉及到数学中的基础集合知识，例如：子集、交集等
bri = set(['brazil', 'russia', 'india'])
print('india in bri is', 'india' in bri)

print('usa in bri is', 'usa' in bri)

bric = bri.copy()
bric.add('china')
bric.issuperset(bri)

print(bri)
print(bric)

bri.remove('russia')

print(bri)
print(bric)

# 交集
print(bri & bric)
