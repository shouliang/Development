# 控制台输入两个数，以空格割开，求两数之和
# http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemId=1
while True:
    try:
        line = input()
        num = line.split()
        print(int(num[0]) + int(num[1]))
    except:
        break
