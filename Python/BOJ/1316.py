def checker(a):
    b = set(a)
    b = list(b)
    b.sort()
    c = []
    for i in a:
        if len(c) == 0:
            c.append(i)
        else:
            if c[len(c) - 1] != i:
                c.append(i)
    c.sort()
    if c == b:
        return True
    else:
        return False

num = int(input())
cnt = 0
for i in range(num):
    s = input()
    a = list(s)
    if checker(a):
        cnt += 1
print(cnt)