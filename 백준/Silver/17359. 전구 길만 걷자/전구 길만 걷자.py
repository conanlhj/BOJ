from itertools import permutations

lights = []
switch = 0
for _ in range(int(input())):
    tmp = input()
    lights.append(tmp[0] + tmp[-1])
    for i in range(len(tmp) - 1):
        if tmp[i] != tmp[i + 1]:
            switch += 1

result = int(1e9)
for case in permutations(lights):
    tmp = 0
    for i in range(len(case) - 1):
        if case[i][1] != case[i + 1][0]:
            tmp += 1
    result = min(result, switch + tmp)
print(result)
