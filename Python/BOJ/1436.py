num = int(input())
find_num = 665
cnt = 0
while cnt != num:
    find_num += 1
    if "666" in str(find_num):
        cnt += 1
print(find_num)