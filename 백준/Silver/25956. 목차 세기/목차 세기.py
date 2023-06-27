N = int(input())
arr = []
nums = [0] * (N+2)
for tmp in [int(input()) for _ in range(N)]:
    if (not arr and tmp != 1) or (arr and arr[-1] + 1 < tmp):
        print(-1)
        exit()
    arr.append(tmp)
stack = []
while arr:
    tmp = arr.pop()
    nums[tmp] += 1
    stack.append(nums[tmp+1])
    nums[tmp+1] = 0
print(*list(reversed(stack)), sep='\n')