import heapq
N = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)])
L, P = map(int, input().split())
idx = 0
heap = []
while idx < N and arr[idx][0] <= P:
    heapq.heappush(heap, -arr[idx][1])
    idx += 1
cnt = 0
while True:
    if P >= L:
        print(cnt)
        break
    if not heap:
        print(-1)
        break
    P -= heapq.heappop(heap)
    cnt += 1
    while idx < N and arr[idx][0] <= P:
        heapq.heappush(heap, -arr[idx][1])
        idx += 1