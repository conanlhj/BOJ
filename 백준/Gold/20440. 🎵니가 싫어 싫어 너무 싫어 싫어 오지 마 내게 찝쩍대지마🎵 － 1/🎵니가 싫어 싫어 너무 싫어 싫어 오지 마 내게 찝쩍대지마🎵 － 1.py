import sys
input = sys.stdin.readline
n = int(input())
d = {}
for _ in range(n):
    te, tx = map(int, input().split())
    if te in d.keys():
        d[te] += 1
    else:
        d[te] = 1
    if tx in d.keys():
        d[tx] -= 1
    else:
        d[tx] = -1

max_val = 0
max_start_idx = -1
max_end_idx = -1
val = 0
sorted_key = sorted(d.keys())
for idx, k in enumerate(sorted(d.keys())):
    val += d[k]
    if val > max_val:
        max_val = val
        max_start_idx = idx
        max_end_idx = idx
    elif val == max_val and max_end_idx == idx - 1:
        max_end_idx = idx
print(max_val)
print(sorted_key[max_start_idx], sorted_key[max_end_idx+1])