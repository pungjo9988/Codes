body = []
rank = []
for i in range(int(input())):
    [a, b] = map(int, input().split())
    body.append([a, b])
for i in range(len(body)):
    cnt = 1
    for j in range(len(body)):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            cnt += 1
    rank.append(cnt)
for i in rank:
    print(i, end=" ")