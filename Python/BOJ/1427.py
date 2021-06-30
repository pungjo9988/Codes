import sys
n = input()
arr = list(map(int, n))
arr.sort(reverse=True)
for i in range(len(arr)):
    print(arr[i], end="")