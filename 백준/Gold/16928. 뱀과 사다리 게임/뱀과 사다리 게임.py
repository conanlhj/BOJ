from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [0] * 101
lines = {}
for _ in range(N + M):
    x, y = map(int, input().split())
    lines[x] = y
Q = deque([1])
while Q:
    x = Q.popleft()
    if x == 100:
        print(visited[-1])
        break
    for d in range(1, 7):
        nx = x + d
        if nx < 101 and visited[nx] == 0:
            if nx in lines.keys():
                nx = lines[nx]
            if visited[nx] == 0:
                visited[nx] = visited[x] + 1
                Q.append(nx)
