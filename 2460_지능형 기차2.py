a = []
for i in range(5):
    a.append(sum(map(int, input().split())))
print(a.index(max(a))+1, max(a))
