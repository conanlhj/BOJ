R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if room[i][0] == -1:
        air_puri = i
        break


def diffusion():
    d = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    result = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                cnt = 0
                for dx, dy in d:
                    nx = dx + i
                    ny = dy + j
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        result[nx][ny] += room[i][j] // 5
                        cnt += 1
                result[i][j] += room[i][j] - (room[i][j] // 5) * cnt
    result[air_puri][0] = -1
    result[air_puri + 1][0] = -1
    return result


def wind():
    d = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    dir = 0
    prev = 0
    x, y = air_puri, 1
    while True:
        if x == air_puri and y == 0:
            break

        nx = x + d[dir][0]
        ny = y + d[dir][1]

        if 0 <= nx < R and 0 <= ny < C:
            room[x][y], prev = prev, room[x][y]
            x, y = nx, ny
        else:
            dir += 1

    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dir = 0
    prev = 0
    x, y = air_puri + 1, 1
    while True:
        if x == air_puri + 1 and y == 0:
            break

        nx = x + d[dir][0]
        ny = y + d[dir][1]

        if 0 <= nx < R and 0 <= ny < C:
            room[x][y], prev = prev, room[x][y]
            x, y = nx, ny
        else:
            dir += 1


for _ in range(T):
    room = diffusion()
    wind()
print(sum(sum(j for j in i) for i in room) + 2)
