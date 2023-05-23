while True:
    s = input()
    if s == "#":
        break
    ans = 0
    for i in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
        ans += s.count(i)
    print(ans)