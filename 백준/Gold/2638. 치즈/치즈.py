from collections import deque

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(sx, sy):
    q = deque([(sx, sy)])
    room[sx][sy] = 2
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                room[nx][ny] = 2
                q.append((nx, ny))


def cheese_remove():
    new_room = [[0] * (M) for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if room[i][j] == 1:
                cnt = 0
                for dx, dy in d:
                    nx = dx + i
                    ny = dy + j
                    if room[nx][ny] == 2:
                        cnt += 1
                if cnt < 2:
                    new_room[i][j] = 1
    return new_room

ans = 0
while any([any(i) for i in room]):
    bfs(0, 0)
    room = cheese_remove()
    ans += 1
print(ans)