N = int(input())
for i in range(N):
    if i == 0 or i == N-1:
        print("*"*N)
        continue
    t = "*"
    for j in range(1, N-1):
        if i == j or N-i == j+1:
            t += "*"
        else:
            t += " "
    t += "*"
    print(t)