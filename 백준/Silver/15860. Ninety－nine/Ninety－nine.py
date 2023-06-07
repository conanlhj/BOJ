print(1)
while True:
    a = int(input())
    if a == 99: break
    ans = a + 3 - (a % 3) if a % 3 else a + 1
    print(ans)
    if ans == 99: break