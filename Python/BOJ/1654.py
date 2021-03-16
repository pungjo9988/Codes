import sys
k, n = map(int, sys.stdin.readline().split())
length = []
for i in range(0, k):
    length.append(int(sys.stdin.readline()))
left = 1
right = max(length)
while left <= right:
    temp = 0
    mid = (left + right) // 2
    for i in length:
        if mid <= i:
            temp += i // mid
    if temp >= n:
        left = mid + 1
    elif temp < n:
        right = mid - 1
print(right)