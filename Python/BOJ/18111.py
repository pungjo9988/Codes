import sys
n, m, b = map(int, sys.stdin.readline().split())
result = [sys.maxsize, 0]
table = []
min_height = 256
for i in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))
    min_height = min(min_height, min(table[i]))
for h in range(min_height, 257):
    time, blocks = 0, b
    for i in range(n):
        for j in range(m):
            if table[i][j] > h:
                time += 2 * (table[i][j] - h)
                blocks += table[i][j] - h
            else:
                time += h - table[i][j]
                blocks -= h - table[i][j]
    if blocks >= 0:
        if time < result[0]:
            result = [time, h]

        elif time == result[0]:
            result[1] = h
    else:
        break
sys.stdout.write(str(result[0]))
sys.stdout.write(' ')
sys.stdout.write(str(result[1]))