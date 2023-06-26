from collections import deque
import sys
input = sys.stdin.readline

q = deque([])
state = 0
bw = [0, 0]
for _ in range(int(input())):
    
    c = input().split()
    if c[0] == "push":
        q.appendleft(c[1])
        bw[c[1]=="w"] += 1
    elif c[0] == "pop":
        if q:
            bw[q.pop()=="w"] -= 1
    elif c[0] == "rotate":
        if c[1] == "l":
            state = (state + 3) % 4
        else:
            state = (state + 1) % 4
    elif c[0] == "count":
        print(bw[c[1]=="w"])

    if state == 1:
        while q:
            tmp = q.pop()
            bw[0] -= 1
            if tmp == "w":
                q.append(tmp)
                bw[0] += 1
                break
    elif state == 3:
        while q:
            tmp = q.popleft()
            bw[0] -= 1
            if tmp == "w":
                q.appendleft(tmp)
                bw[0] += 1
                break