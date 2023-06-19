stack = []
ans = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    while stack and b < stack[-1]:
        ans += 1
        stack.pop()
    if not stack or stack[-1] != b:
        stack.append(b)
while stack:
    if stack[-1]:
        ans += 1
    stack.pop()
print(ans)