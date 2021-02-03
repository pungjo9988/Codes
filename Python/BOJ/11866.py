import sys
k, n = map(int, sys.stdin.readline().split())
arr = [x for x in range(1, k + 1)]
print_arr = []
cnt = n - 1
while len(print_arr) != k:
    if cnt >= len(arr):
        cnt = cnt % len(arr)
    print_arr.append(arr[cnt])
    del arr[cnt]
    cnt += n - 1
print('<', end='')
for i in print_arr:
    if i == print_arr[-1]:
        print(i, end='>')
    else:
        print(i, end=', ')