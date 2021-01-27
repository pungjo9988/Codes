import sys
_ = sys.stdin.readline()
N = list(map(int, sys.stdin.readline().split()))
_ = sys.stdin.readline()
M = list(map(int, sys.stdin.readline().split()))
dic = {}
for i in N:
    try:
        dic[i] += 1
    except:
        dic[i] = 1
answer = []
for j in M:
    try:
        answer.append(dic[j])
    except:
        answer.append(0)
for i in answer:
    print(i, end=" ")