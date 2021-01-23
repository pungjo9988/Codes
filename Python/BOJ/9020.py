num_arr = [True] * 10000
for i in range(2, 101):
    if num_arr[i]:
        for j in range(2 * i, 10000, i):
            num_arr[j] = False

for i in range(int(input())):
    num = int(input())
    for j in range(num//2, 1, -1):
        if num_arr[j] and num_arr[num - j]:
            print(j, num - j)
            break
