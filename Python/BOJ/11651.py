import sys
pos = []
for i in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    pos.append([x, y])
pos = sorted(pos, key = lambda x: (x[1], x[0]))
for i in range(len(pos)):
    print(pos[i][0], pos[i][1])