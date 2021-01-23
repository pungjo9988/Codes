num = int(input())
score = map(int, input().split())
score = list(score)
Max = max(score)
aver = 0
for i in range(len(score)):
    aver += score[i] / Max * 100
print(aver / num)