import sys
cnt = int(input())
arr = []
for i in range(cnt):
    arr.append(int(sys.stdin.readline()))
for i in sorted(arr):
    print(i)