import sys
N, M = map(int, sys.stdin.readline().split())
poke1 = {}
poke2 = {}
for i in range(N):
    poke_name = str(sys.stdin.readline().strip())
    poke1[i + 1] = poke_name
    poke2[poke_name] = i + 1
for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    if temp.isdigit():
        print(poke1[int(temp)])
    else:
        print(poke2[temp])