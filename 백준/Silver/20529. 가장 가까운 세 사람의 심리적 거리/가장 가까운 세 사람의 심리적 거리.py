from itertools import combinations


mbtis = {
    "ISTJ": 0,
    "ISTP": 1,
    "ISFJ": 2,
    "ISFP": 3,
    "INTJ": 4,
    "INTP": 5,
    "INFJ": 6,
    "INFP": 7,
    "ESTJ": 8,
    "ESTP": 9,
    "ESFJ": 10,
    "ESFP": 11,
    "ENTJ": 12,
    "ENTP": 13,
    "ENFJ": 14,
    "ENFP": 15,
}

dist = [[0] * 16 for _ in range(16)]
for a in mbtis.values():
    for b in mbtis.values():
        dist[a][b] = sum(map(int, bin(a ^ b)[2:]))

for t in range(int(input())):
    N = int(input())
    arr = input().split()
    if N > 32:
        print(0)
        continue

    min_dist = int(1e9)
    for case in combinations(arr, 3):
        case = list(map(lambda x: mbtis[x], case))
        total_dist = (
            dist[case[0]][case[1]] + dist[case[1]][case[2]] + dist[case[0]][case[2]]
        )
        min_dist = min(min_dist, total_dist)
    print(min_dist)