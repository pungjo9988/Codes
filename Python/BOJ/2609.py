a, b = map(int, input().split())
temp1 = max(a, b)
temp2 = min(a, b)
while(True):
    c = temp1 % temp2
    if c == 0:
        print(temp2)
        break
    temp1 = temp2
    temp2 = c
print(a * b // temp2)