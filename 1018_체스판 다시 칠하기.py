def makeboard(i, j):
    b = []
    for _ in range(8):
        b.append(board[i+_][j:j+8])
    return b


n, m = map(int, input().split())
board = [input() for i in range(n)]
cnt = []
for k in range(n-7):
    for s in range(m-7):
        b = makeboard(k, s)
        # 왼쪽 위가 B인 경우.
        cnt_w = 0
        for i in range(8):
            for j in range(8):
                if (i+j) % 2:
                    if b[i][j] != 'W':
                        cnt_w += 1
                else:
                    if b[i][j] != 'B':
                        cnt_w += 1
        cnt.append(min(cnt_w, 64-cnt_w))
print(min(cnt))
