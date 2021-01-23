for i in range(int(input())):
    k = int(input())
    n = int(input())
    apt = [a for a in range(1, n + 1)]
    for h in range(k):
        for w in range(1, n):
            apt[w] += apt[w-1]
    print(apt[-1])