N, X = map(int, input().split())
result = 0
menu = []
for _ in range(N):
    a, b = map(int, input().split())
    result += b
    menu.append(a - b)
    X -= 1000
menu.sort(reverse=True)

for _ in range(N):
    if X < 4000:
        break
    elif menu[_] > 0:
        result += menu[_]
        X -= 4000

print(result)
