row, col = map(int, input().split())
board = []
for i in range(row):
    board.append(input())

min = 64

for i in range(row - 7):
    for j in range(col - 7):
        white_cnt = 0
        black_cnt = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] == "W":
                        white_cnt += 1
                    if board[a][b] == "B":
                        black_cnt += 1
                else:
                    if board[a][b] == "B":
                        white_cnt += 1
                    if board[a][b] == "W":
                        black_cnt += 1
        temp = white_cnt if white_cnt > black_cnt else black_cnt
        if min > 64 - temp:
            min = 64 - temp
print(min) 