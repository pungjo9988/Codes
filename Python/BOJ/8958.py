for i in range(int(input())):
    arr = list(input())
    answer = 0
    cnt = 0
    for j in arr:
        if j == 'O':
            cnt += 1
        else:
            cnt = 0
        answer += cnt
    print(answer)