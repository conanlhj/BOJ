n = int(input())
cranes = sorted(map(int, input().split()), reverse=True)
m = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

if max(boxes) > max(cranes):
    print(-1)
    exit()
    
cnt = 0
while boxes:
    for c in cranes:
        for i in range(m):
            if c >= boxes[i]:
                del boxes[i]
                m -= 1
                break
    cnt += 1
print(cnt)