n = int(input())
t_result = [int(input()) for _ in range(n)]
stack, result = [], []
cnt, i = 0, 1
r = []
flag = True

while result != t_result:
    if len(stack) == 0:
        stack.append(i)
        i += 1
        r.append('+')
    if t_result[cnt] == stack[-1]:
        result.append(stack.pop())
        cnt += 1
        r.append('-')
    else:
        stack.append(i)
        i += 1
        r.append('+')
    if i > n+1:
        flag = False
        break

if flag:
    print(*r, sep='\n')
else:
    print('NO')
