words = [input() for _ in range(int(input()))]
length = [len(_) for _ in words]

result = []
for i in range(1, max(length)+1):
    tmp = set()
    for j in range(len(words)):
        if length[j] == i:
            tmp.add(words[j])
    tmp = sorted(tmp)
    for j in tmp:
        result.append(j)
print(*result, sep='\n')
