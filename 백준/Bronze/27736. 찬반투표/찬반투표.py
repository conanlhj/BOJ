input()
a = [0, 0, 0]
for i in list(map(int, input().split())):
    a[i + 1] += 1
if sum(a) / 2 <= a[1]:
    print("INVALID")
elif a[0] < a[2]:
    print("APPROVED")
else:
    print("REJECTED")