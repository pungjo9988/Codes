import sys
n = int(sys.stdin.readline())
s = []
a = []
count = 1
no_mes = True
for i in range(0, n):
    num = int(sys.stdin.readline())
    while count <= num:
        s.append(count)
        a.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        a.append('-')
    else:
        no_mes = False
if no_mes == False:
    print('NO')
else:
    for i in a:
        print(i)