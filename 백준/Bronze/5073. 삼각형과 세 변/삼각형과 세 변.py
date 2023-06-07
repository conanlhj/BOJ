while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if 2 * max(a, b, c) >= sum([a, b, c]):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif len(set([a, b, c])) == 2:
        print("Isosceles")
    else:
        print("Scalene")