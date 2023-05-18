def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, u, v):
    u = find_parent(parent, u)
    v = find_parent(parent, v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v


v = int(input())
planets_x = []
planets_y = []
planets_z = []
for i in range(v):
    x, y, z = map(int, input().split())
    planets_x.append((x, i))
    planets_y.append((y, i))
    planets_z.append((z, i))

planets_x.sort()
planets_y.sort()
planets_z.sort()

edges = []
parent = list(range(v))

for i in range(v - 1):
    edges.append(
        (planets_x[i + 1][0] - planets_x[i][0], planets_x[i][1], planets_x[i + 1][1])
    )
    edges.append(
        (planets_y[i + 1][0] - planets_y[i][0], planets_y[i][1], planets_y[i + 1][1])
    )
    edges.append(
        (planets_z[i + 1][0] - planets_z[i][0], planets_z[i][1], planets_z[i + 1][1])
    )

result = 0
edges.sort()
for edge in edges:
    cost, u, v = edge
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += cost

print(result)
