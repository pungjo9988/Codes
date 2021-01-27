import sys
arr = []
sum = 0
cnt = [0] * 8001
a = int(sys.stdin.readline())
for i in range(a):
    num = int(sys.stdin.readline())
    arr.append(num)
    sum += num
    cnt[num + 4000] += 1
print(round(sum/a))
arr = sorted(arr)
print(arr[a//2])
num = max(cnt)
temp = []
for i in range(8001):
    if cnt[i] == num:
        temp.append(i)
temp = sorted(temp)
if len(temp) > 1:
    print(temp[1] - 4000)
else:
    print(temp[0] - 4000)
print(arr[-1] - arr[0])