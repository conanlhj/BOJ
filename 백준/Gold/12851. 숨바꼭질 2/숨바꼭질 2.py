from collections import deque

N, K = map(int, input().split())
visited = [0] * (100001)
visited[N] = True

q = deque([(N, 0)])
cnt = 0
min_val = 100001
while q:
    x, c = q.popleft()
    
    if x == K:
        if min_val == 100001:
            min_val = c
        
        if c == min_val:
            cnt += 1
    
    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx < 100001 and (visited[nx] == 0 or visited[nx] == c+1):
            visited[nx] = c + 1
            q.append((nx, c + 1))
            
print(min_val)
print(cnt)