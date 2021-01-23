arr = [False] * 42
cnt = 0
for i in range(10):
    num = int(input())
    arr[num % 42] = True
for i in range(42):
    if arr[i]:
        cnt += 1
print(cnt)