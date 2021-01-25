# Sol 1
f = 1
for i in range(2, int(input())+1):
    f *= i
sf = str(f)
for i in range(len(sf)):
    if sf[len(sf)-i-1] != '0':
        print(i)
        break

# Sol 2
n = int(input())
print(n//5+n//25+n//125)
