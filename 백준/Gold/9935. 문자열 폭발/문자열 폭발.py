from collections import deque

stack = []
S = input()
ex = input()
ex_len = len(ex)

for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-ex_len:]) == ex:
        for _ in range(ex_len):
            stack.pop()
    
print("".join(stack) if stack else "FRULA")