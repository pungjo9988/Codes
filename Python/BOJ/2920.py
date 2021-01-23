paino = ['1', '2', '3', '4', '5', '6', '7', '8']
re_paino = ['1', '2', '3', '4', '5', '6', '7', '8']
re_paino.reverse()
temp = list(input().split())
if paino == temp:
    print('ascending')
elif re_paino == temp:
    print('descending')
else:
    print('mixed')