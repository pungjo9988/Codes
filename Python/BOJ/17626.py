import sys
import math
num = int(sys.stdin.readline())
min_num = 4
for i in range(int(math.sqrt(num)), int(math.sqrt(num/4)), -1):
    if i * i == num:
        min_num = 1
        break
    else:
        temp = num - i * i
        for j in range(int(math.sqrt(temp)), int(math.sqrt(temp/3)), -1):
            if i*i + j*j == num:
                min_num = min(min_num, 2)
                break
            else:
                temp = num - i*i - j*j
                for k in range(int(math.sqrt(temp)), int(math.sqrt(temp/2)), -1):
                    if i*i + j*j + k*k == num:
                        min_num = min(min_num, 3)
print(min_num)