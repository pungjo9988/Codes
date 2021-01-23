for i in range(int(input())):
    temp = input().split()
    num = ord(temp[0]) - 48
    S = list(temp[1])
    for i in S:
        for a in range(num):
            print(i, end="")
    print()