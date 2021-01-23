a = input()
leng = len(a)
a = int(a)
cnt = 0
if leng <= 2:
    cnt = a
elif leng == 3:
    cnt = 99
    for i in range(100, a + 1):
        if i // 100 - i // 10 % 10 == i // 10 % 10 - i % 10:
            cnt += 1
elif leng == 4:
    cnt = 144
    for i in range(1000, a + 1):
        if i // 1000 - i // 100 % 10 == i // 100 % 10 - i // 10 % 10 == i // 10 % 10 - i % 10:
            cnt += 1
print(cnt)