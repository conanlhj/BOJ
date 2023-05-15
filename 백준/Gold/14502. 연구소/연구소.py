from itertools import combinations
from collections import deque

N, M = map(int, input().split())
room = []
virus = []
empty = []
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for _ in range(N):
    tmp = list(map(int, input().split()))
    room.append(tmp)
    for i in range(M):
        if tmp[i] == 2:
            virus.append((_, i))
        elif tmp[i] == 0:
            empty.append((_, i))

ans = 0
for p in combinations(empty, 3):
    new_room = [[i for i in j] for j in room]
    for x, y in p:
        new_room[x][y] = 1
    
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and new_room[nx][ny] == 0:
                new_room[nx][ny] = 2
                q.append((nx, ny))
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_room[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)
print(ans)