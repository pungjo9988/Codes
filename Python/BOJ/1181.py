arr = []
for i in range(int(input())):
    arr.append(input())
arrs = list(set(arr))
sort_arr = []
for i in arrs:
    sort_arr.append((len(i), i))
sort_arr.sort()
for len_voca, voca in sort_arr:
    print(voca)
