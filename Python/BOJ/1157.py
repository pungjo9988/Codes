sent = input()
arr = list(sent)
cnt = [0] * 26
for i in arr:
    j = (ord(i) - 65) % 32
    cnt[j] = cnt[j] + 1
max = 0
spell = '?'
for i in range(26):
    if cnt[i]>max:
        max = cnt[i]
        spell = chr(i+65)
    elif cnt[i] == max:
        spell = '?'
print(spell) 