import sys
trees, need = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))
left = 1
right = max(height)
temp = 0
while left <= right:
    temp = 0
    mid = (left + right) // 2
    for i in height:
        if mid < i:
            temp += i - mid
    if temp >= need:
        left = mid + 1
    elif temp < need:
        right = mid - 1
print(right)