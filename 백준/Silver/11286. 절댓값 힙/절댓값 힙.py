import heapq
import sys
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(h, (abs(x), x))
    elif h:
        print(heapq.heappop(h)[1])
    else:
        print(0)
