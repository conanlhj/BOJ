def findSpot(line):
    spotcnt = 0
    cnt = 0
    for i in range(n):
        if line[i] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                spotcnt += 1
            cnt = 0
    if cnt >= 2:
        spotcnt += 1
    return spotcnt


n = int(input())
room = [input() for i in range(n)]
spot_h = 0
spot_v = 0
for i in range(n):
    spot_h += findSpot(room[i])
for i in list(zip(*room)):
    spot_v += findSpot(''.join(i))
print(spot_h, spot_v)
