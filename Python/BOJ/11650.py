import sys
pos = []
cnt = int(input())
for i in range(cnt):
    [a, b] = map(int, sys.stdin.readline().split())
    pos.append([a, b])
pos = sorted(pos)
for i in range(cnt):
    print(pos[i][0], pos[i][1])