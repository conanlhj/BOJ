from collections import deque

a = deque(list(input()))
b = deque([])

for _ in range(int(input())):
    com = input()
    if com == "L" and a:
        b.appendleft(a.pop())
    elif com == "D" and b:
        a.append(b.popleft())
    elif com == "B" and a:
        a.pop()
    elif com[0] == "P":
        a.append(com[-1])
print("".join(a + b))
