find = int(input())
a = b = 0
while find > a:
    b += 1
    a += b
a -= b
c = find - a
if b % 2 == 1:
    print(b - c + 1, end='/')
    print(c)
elif b % 2 == 0:
    print(c, end='/')
    print(b - c + 1)