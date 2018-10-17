bri = set(['brazil', 'russia', 'india'])
print('india in bri is','india' in bri)

print('usa in bri is','usa' in bri)

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