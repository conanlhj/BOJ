N, M = map(int, input().split())
r, c, d = map(int, input().split())
clean = [list(map(int, input().split())) for _ in range(N)]
dr = [(0, -1), (1, 0), (0, 1), (-1, 0)]
d = 3 - d
ans = 0
while True:
    if not clean[r][c]:
        clean[r][c] = 2
        ans += 1

    if all([clean[dx + r][dy + c] for dx, dy in dr]):
        dx, dy = dr[(d + 2) % 4]
        nx, ny = dx + r, dy + c
        if clean[nx][ny] != 1:
            r, c = nx, ny
        else:
            break
    else:
        while True:
            d = (d + 1) % 4
            dx, dy = dr[d]
            nx, ny = dx + r, dy + c
            if not clean[nx][ny]:
                r, c = nx, ny
                break
print(ans)