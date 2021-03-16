import sys
count = int(sys.stdin.readline())
for i in range(count):
    cnt = 1
    n, m = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    while True:
        if num[m] == max(num):
            if m == 0:
                print(cnt)
                break
            elif num[0] != max(num):
                num.append(num.pop(0))
                m -= 1
            elif num[0] == max(num):
                cnt += 1
                num.pop(0)
                m -= 1
        elif num[0] == max(num):
            num.pop(0)
            cnt += 1
            m -= 1
            if m < 0:
                m = len(num) - 1
        elif num[0] != max(num):
            num.append(num.pop(0))
            m -= 1
            if m < 0:
                m = len(num) - 1