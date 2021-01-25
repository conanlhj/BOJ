for t in range(int(input())):
    a, b = map(int, input().split())
    c = [(a**_)%10 for _ in range(1, 5)][b % 4-1]
    print(c if c else 10)
