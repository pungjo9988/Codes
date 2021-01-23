s = list(input())
alpa = [-1] * 26
for i in s:
    for j in range(97, 123):
        if i == chr(j):
            alpa[j - 97] = s.index(chr(j))
for i in range(26):
    print(alpa[i], end=" ") 