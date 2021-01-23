def fact(num):
    answer = 1
    for i in range(num + 1):
        if i == 0:
            continue
        answer *= i
    return answer

count = int(input())
answer = [0] * count
for i in range(count):
    left, right = map(int, input().split())
    if right -left == 0:
        answer[i] = 1
    else:
        answer[i] = fact(right) // fact(left) // fact(right - left)

for i in range(count):
    print(int(answer[i]))