a, b = map(int, input().split())
section = [0, 1]
i = 1
while section[-1] < 1000:
    i += 1
    section.append(section[-1]+i)
res = 0
for i in range(a, b+1):
    for j in range(len(section)):
        if i <= section[j]:
            res += j
            break
print(res)
